# Sync from BF-Vault (Obsidian) to BF-Vault-Web/content (Quartz)
# Usage: ./sync-from-vault.ps1 [-Push]

param(
    [switch]$Push
)

$VAULT_PATH = "C:\Users\bfipa\Documents\BF-Vault"
$CONTENT_PATH = "C:\Users\bfipa\Documents\BF-Vault-Web\content"

Write-Host "Syncing BF-Vault -> BF-Vault-Web/content..." -ForegroundColor Cyan

# Check if vault exists
if (-not (Test-Path $VAULT_PATH)) {
    Write-Host "ERROR: BF-Vault not found: $VAULT_PATH" -ForegroundColor Red
    exit 1
}

# Create content folder if not exists
if (-not (Test-Path $CONTENT_PATH)) {
    New-Item -ItemType Directory -Path $CONTENT_PATH -Force | Out-Null
}

# Sync using robocopy
$result = robocopy $VAULT_PATH $CONTENT_PATH /MIR /XD .obsidian .git private /XF .gitignore /R:0 /W:0 /NP /NDL 2>&1
$exitCode = $LASTEXITCODE

# robocopy exit codes: 0-7 = success, 8+ = error
if ($exitCode -gt 7) {
    Write-Host "ERROR: Sync failed with exit code: $exitCode" -ForegroundColor Red
    exit 1
}

# Count changes
$filesCopied = ($result | Select-String "New File|Newer|Older").Count
$filesDeleted = ($result | Select-String "Extra File").Count

if ($filesCopied -eq 0 -and $filesDeleted -eq 0) {
    Write-Host "Already in sync - no changes" -ForegroundColor Green
} else {
    Write-Host "Synced: $filesCopied files copied, $filesDeleted files removed" -ForegroundColor Green
}

# Git operations in BF-Vault-Web
Set-Location "C:\Users\bfipa\Documents\BF-Vault-Web"

$status = git status --short 2>&1
if ($status) {
    Write-Host ""
    Write-Host "Changes detected:" -ForegroundColor Yellow
    Write-Host $status

    if ($Push) {
        Write-Host ""
        Write-Host "Committing and pushing..." -ForegroundColor Cyan

        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
        git add .
        git commit -m "sync: Update content from BF-Vault ($timestamp)"
        git push origin main

        Write-Host "Pushed to GitHub - Vercel will rebuild" -ForegroundColor Green
        Write-Host "Site: https://bf-knowledge-base.vercel.app/" -ForegroundColor Cyan
    } else {
        Write-Host ""
        Write-Host "Run with -Push to commit and push:" -ForegroundColor Yellow
        Write-Host "  ./sync-from-vault.ps1 -Push"
    }
} else {
    Write-Host ""
    Write-Host "No changes to commit" -ForegroundColor Green
}
