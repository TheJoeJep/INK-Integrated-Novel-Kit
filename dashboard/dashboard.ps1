<#
.SYNOPSIS
    Launch the story dashboard.

.EXAMPLE
    .\dashboard.ps1
    .\dashboard.ps1 -StoryPath "E:\Writing\Some Other Novel" -Port 8080
#>
param(
    [string]$StoryPath = "path\to\your-novel",
    [int]$Port = 8778,
    [switch]$NoBrowser
)
$ErrorActionPreference = 'Stop'
if (-not (Test-Path $StoryPath)) { throw "Workspace not found: $StoryPath" }

$py = (Get-Command python -ErrorAction SilentlyContinue)
if (-not $py) { throw "Python not found on PATH." }

Push-Location $PSScriptRoot
try {
    $args = @("serve.py", $StoryPath, $Port)
    if (-not $NoBrowser) { $args += "--open" }
    & python @args
} finally {
    Pop-Location
}
