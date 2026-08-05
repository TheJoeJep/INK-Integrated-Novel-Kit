<#
.SYNOPSIS
    Copies the canonical engine files into a story workspace.

.DESCRIPTION
    The engine is the single source of truth for craft/, skills/, and templates/.
    A story workspace holds REAL COPIES of those (not junctions), so that both
    directories are ordinary git repositories that clone and zip correctly.

    Direction is one-way: engine -> story. Anything you change in the story
    workspace's craft/ or .claude/ folders is OVERWRITTEN. Edit the engine.

.PARAMETER StoryPath
    The story workspace to sync into.

.PARAMETER WhatIf
    Show what would change without writing anything.

.EXAMPLE
    .\sync-to-story.ps1
    .\sync-to-story.ps1 -StoryPath "E:\Writing\Some Other Novel" -WhatIf
#>

[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$StoryPath
)

$ErrorActionPreference = 'Stop'
$engine = $PSScriptRoot

# Default target lives in a gitignored local file so the repo ships with no
# machine-specific paths in it. Create ink.local.json next to this script:
#     { "storyPath": "E:\\Writing\\My Novel" }
if (-not $StoryPath) {
    $cfgPath = Join-Path $engine "ink.local.json"
    if (Test-Path $cfgPath) {
        $cfg = Get-Content $cfgPath -Raw | ConvertFrom-Json
        $StoryPath = $cfg.storyPath
    }
}

if (-not $StoryPath) {
    throw "No story workspace given. Pass -StoryPath, or create ink.local.json with { `"storyPath`": `"...`" }"
}
if (-not (Test-Path $StoryPath)) { throw "Story workspace not found: $StoryPath" }

# source -> destination, relative to $engine and $StoryPath
$pairs = @(
    @{ From = "craft";              To = "craft";              What = "craft knowledge base" },
    @{ From = "skills";             To = ".claude\skills";     What = "skills" },
    @{ From = "templates";          To = ".claude\templates";  What = "document templates" },
    @{ From = "docs\sources\notes"; To = "sources\notes";      What = "extraction notes" }
)

# Single files
$files = @(
    @{ From = "docs\sources\PROCESSING-LOG.md"; To = "sources\PROCESSING-LOG.md" },
    @{ From = "CREDITS.md";                     To = "CREDITS.md" }
)

Write-Host ""
Write-Host "  engine : $engine"
Write-Host "  story  : $StoryPath"
Write-Host ""

foreach ($p in $pairs) {
    $src = Join-Path $engine $p.From
    $dst = Join-Path $StoryPath $p.To
    if (-not (Test-Path $src)) { Write-Warning "missing in engine, skipped: $($p.From)"; continue }

    if ($PSCmdlet.ShouldProcess($dst, "mirror from $($p.From)")) {
        New-Item -ItemType Directory -Force -Path $dst | Out-Null
        # /MIR mirrors: destination becomes an exact copy. Local edits there are discarded by design.
        $null = robocopy $src $dst /MIR /NFL /NDL /NJH /NJS /NP /R:2 /W:1
        if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE) for $($p.From)" }
        $n = (Get-ChildItem $dst -Recurse -File | Measure-Object).Count
        "{0,-22} {1,4} files" -f $p.What, $n
    }
}

foreach ($f in $files) {
    $src = Join-Path $engine $f.From
    $dst = Join-Path $StoryPath $f.To
    if (-not (Test-Path $src)) { Write-Warning "missing in engine, skipped: $($f.From)"; continue }
    if ($PSCmdlet.ShouldProcess($dst, "copy")) {
        New-Item -ItemType Directory -Force -Path (Split-Path $dst) | Out-Null
        Copy-Item -LiteralPath $src -Destination $dst -Force
        "{0,-22} {1}" -f "single file", $f.To
    }
}

Write-Host ""
Write-Host "  NOT synced (engine only): docs\sources\transcripts, docs\sources\raw-vtt"
Write-Host "  These are ~440k words of lecture captions. They stay out of story repos"
Write-Host "  and must never be published. See docs\DISTRIBUTION-PLAN.md"
Write-Host ""
Write-Host "  Done."
Write-Host ""

# robocopy uses low exit codes for success (1 = files copied). Don't leak that as failure.
exit 0
