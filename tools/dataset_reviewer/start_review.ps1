$ErrorActionPreference = "Stop"

$reviewerRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Push-Location $reviewerRoot
try {
    python tools/dataset_reviewer/server.py --open
}
finally {
    Pop-Location
}
