<#
    Stop hook — speaks Claude's reply aloud using Windows' built-in speech synthesiser.

    No install, no API key, no dependencies. System.Speech ships with .NET on Windows.

    Reads the hook payload on stdin, pulls the last assistant message out of the
    transcript, strips everything that doesn't belong in speech, and speaks it.

    Two ways to control what gets said:
      1. Put <speak>...</speak> anywhere in a reply and ONLY that is spoken.
      2. Otherwise the reply is cleaned and truncated to $MaxChars.

    Never speaks: code blocks, tables, file paths, receipt blocks, URLs.
#>
param(
    [int]$MaxChars = 700,
    [int]$Rate     = 1,      # -10 slowest .. 10 fastest
    [string]$Voice = ""      # e.g. "Microsoft Zira Desktop"; empty = system default
)

$ErrorActionPreference = 'SilentlyContinue'

# ── read the hook payload ────────────────────────────────────────────────────
$raw = [Console]::In.ReadToEnd()
if (-not $raw) { exit 0 }

try { $hook = $raw | ConvertFrom-Json } catch { exit 0 }
$transcript = $hook.transcript_path
if (-not $transcript -or -not (Test-Path $transcript)) { exit 0 }

# ── last assistant message from the JSONL transcript ─────────────────────────
$text = $null
$lines = Get-Content $transcript -Tail 60 -ErrorAction SilentlyContinue
for ($i = $lines.Count - 1; $i -ge 0; $i--) {
    try { $o = $lines[$i] | ConvertFrom-Json } catch { continue }
    if ($o.type -ne 'assistant') { continue }
    $parts = @($o.message.content | Where-Object { $_.type -eq 'text' } | ForEach-Object { $_.text })
    if ($parts.Count) { $text = ($parts -join "`n"); break }
}
if (-not $text) { exit 0 }

# ── explicit <speak> wins ────────────────────────────────────────────────────
$m = [regex]::Match($text, '(?s)<speak>(.*?)</speak>')
if ($m.Success) {
    $say = $m.Groups[1].Value
} else {
    $say = $text
    # things that are unbearable read aloud
    $say = [regex]::Replace($say, '(?s)```.*?```', ' ')            # code fences
    $say = [regex]::Replace($say, '(?m)^\s*[│├└─┌┐┘\|].*$', ' ')   # tables, box drawing
    $say = [regex]::Replace($say, '(?m)^──.*$', ' ')               # receipt blocks
    $say = [regex]::Replace($say, '(?m)^\s*\|.*\|\s*$', ' ')       # markdown tables
    $say = [regex]::Replace($say, 'https?://\S+', ' ')             # urls
    $say = [regex]::Replace($say, '`[^`]*`', ' ')                  # inline code
    $say = [regex]::Replace($say, '[A-Za-z]:\\[^\s]+', ' ')        # windows paths
    $say = [regex]::Replace($say, '\S+\.(md|py|ps1|json|html|js|css)\b', ' ')
    $say = [regex]::Replace($say, '(?m)^\s{0,3}#{1,6}\s*', '')     # headings
    $say = $say -replace '\*\*|\*|__|~~', ''                       # emphasis
    $say = [regex]::Replace($say, '\[([^\]]*)\]\([^)]*\)', '$1')   # links -> text
    $say = [regex]::Replace($say, '[✓✗⚠◷●○→←↳—–]', ' ')
    $say = [regex]::Replace($say, '\s{2,}', ' ')
    $say = $say.Trim()

    if ($say.Length -gt $MaxChars) {
        $cut = $say.Substring(0, $MaxChars)
        $stop = $cut.LastIndexOfAny([char[]]@('.', '?', '!'))
        if ($stop -gt 200) { $say = $cut.Substring(0, $stop + 1) } else { $say = $cut + '...' }
    }
}

if (-not $say -or $say.Length -lt 12) { exit 0 }

# ── speak ────────────────────────────────────────────────────────────────────
try {
    Add-Type -AssemblyName System.Speech
    $s = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $s.Rate = $Rate
    if ($Voice) { try { $s.SelectVoice($Voice) } catch {} }
    $s.Speak($say)
    $s.Dispose()
} catch {}

exit 0
