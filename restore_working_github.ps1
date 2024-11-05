# restore_working_github.ps1
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$gitConfigPath = "$env:USERPROFILE\.gitconfig"
if (Test-Path $gitConfigPath) {
    Remove-Item $gitConfigPath
    Write-Output ".gitconfig removed"
} else {
    Write-Output ".gitconfig not found"
}

git config --global user.email "seredadanil944@gmail.com"
git config --global user.name "Sereda Danil"

$url = "https://github.com/DanilSereda22/ychebproekt"

echo "url=$url" | git credential reject

Write-Output "The script was executed successfully!"

