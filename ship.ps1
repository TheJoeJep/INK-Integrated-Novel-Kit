<#
.SYNOPSIS
    Commit and push whichever repos have changes, in the right order.

.DESCRIPTION
    There are two repositories and one dependency between them:

        ink (engine)  --sync-->  story workspace

    So an engine change must be committed, synced, and then committed again in
    the story repo. A story change touches only the story repo.

    This works out which case applies and does the whole thing safely:

      * refuses to push the engine if any story content has crept into it
      * refuses to push the story repo if its remote is not the expected one
      * skips repos with nothing to commit

.EXAMPLE
    .\ship.ps1 "Fix the pacing skill's output format"
    .\ship.ps1 "Chapter 1 beats 1-3" -StoryOnly
    .\ship.ps1 -DryRun
#>
param(
    [Parameter(Position = 0)][string]$Message,
    [switch]$EngineOnly,
    [switch]$StoryOnly,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'
$engine = $PSScriptRoot

# git writes progress and advisory notices to stderr. Under ErrorActionPreference
# 'Stop', PowerShell turns those into terminating NativeCommandErrors even when
# git exited 0. Run git through this and judge it by its exit code instead.
function git-quiet {
    $out = & git @args 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "git $($args -join ' ') failed ($LASTEXITCODE):`n$($out -join "`n")"
    }
    return $out
}

$cfgPath = Join-Path $engine "ink.local.json"
if (-not (Test-Path $cfgPath)) { throw "ink.local.json not found. It must set storyPath." }
$story = (Get-Content $cfgPath -Raw | ConvertFrom-Json).storyPath
if (-not (Test-Path $story)) { throw "Story workspace not found: $story" }

function Dirty($path) {
    Push-Location $path
    try { return @(git status --porcelain 2>$null).Count -gt 0 } finally { Pop-Location }
}

function Show($path, $label) {
    Push-Location $path
    try {
        $files = @(git status --porcelain 2>$null)
        Write-Host "`n  $label - $($files.Count) change(s)" -ForegroundColor Cyan
        $files | Select-Object -First 12 | ForEach-Object { "      $_" }
        if ($files.Count -gt 12) { "      ... and $($files.Count - 12) more" }
    } finally { Pop-Location }
}

# ── safety: nothing private may reach the public repo ────────────────────────
function AuditEngine {
    Push-Location $engine
    try {
        git-quiet add -A | Out-Null
        $staged = @(git diff --cached --name-only 2>$null)
        $bad = $staged | Where-Object {
            $_ -match 'transcript|raw-vtt|sources/notes|ink\.local|manuscript/|archive/'
        }
        if ($bad) {
            Write-Host "`n  REFUSING TO PUSH - private material staged in the public repo:" -ForegroundColor Red
            $bad | ForEach-Object { "      $_" }
            throw "Aborted. Fix .gitignore before shipping."
        }
    } finally { Pop-Location }
}

function CheckStoryRemote {
    Push-Location $story
    try {
        $r = git remote get-url origin 2>$null
        if ($r -and $r -match 'INK-Integrated-Novel-Kit') {
            throw "The story repo's remote points at the PUBLIC engine repo. Aborted."
        }
    } finally { Pop-Location }
}

function Commit($path, $msg, $label) {
    Push-Location $path
    try {
        git-quiet add -A | Out-Null
        if (@(git diff --cached --name-only 2>$null).Count -eq 0) {
            Write-Host "  $label - nothing to commit" -ForegroundColor DarkGray
            return $false
        }
        git-quiet commit -q -m $msg | Out-Null
        git-quiet push -q | Out-Null
        Write-Host "  $label - committed and pushed" -ForegroundColor Green
        return $true
    } finally { Pop-Location }
}

# ── work out what changed ────────────────────────────────────────────────────
$engineDirty = (Dirty $engine) -and (-not $StoryOnly)
$storyDirty  = (Dirty $story)  -and (-not $EngineOnly)

if (-not $engineDirty -and -not $storyDirty) {
    Write-Host "`n  Nothing to ship. Both repos are clean.`n" -ForegroundColor DarkGray
    exit 0
}

if ($engineDirty) { Show $engine "ink (engine, PUBLIC)" }
if ($storyDirty)  { Show $story  "story (PRIVATE)" }

if ($DryRun) { Write-Host "`n  dry run - nothing committed`n"; exit 0 }

if (-not $Message) { $Message = Read-Host "`n  Commit message" }
if (-not $Message) { throw "A commit message is required." }

CheckStoryRemote

Write-Host ""
if ($engineDirty) {
    AuditEngine
    [void](Commit $engine $Message "ink       ")
    & (Join-Path $engine "sync-to-story.ps1") | Out-Null
    Write-Host "  synced     - engine copied into the story workspace" -ForegroundColor DarkGray
    [void](Commit $story "Sync engine: $Message" "story     ")
} else {
    [void](Commit $story $Message "story     ")
}

Write-Host "`n  Done.`n"
