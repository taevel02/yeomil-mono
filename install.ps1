# PowerShell script to install Yeomil Mono per-user on Windows
$ErrorActionPreference = 'Stop'

# Define directories
$FontFolder = "$env:USERPROFILE\AppData\Local\Microsoft\Windows\Fonts"
if (-not (Test-Path $FontFolder)) {
    New-Item -Path $FontFolder -ItemType Directory | Out-Null
}

$Fonts = @("Regular", "Bold", "Light")
$BaseUrl = "https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/fonts/ttf"
$RegPath = "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Fonts"

foreach ($Weight in $Fonts) {
    $FileName = "YeomilMono-$Weight.ttf"
    $Destination = Join-Path $FontFolder $FileName
    
    Write-Host "Downloading $FileName..."
    Invoke-WebRequest -Uri "$BaseUrl/$FileName" -OutFile $Destination -UseBasicParsing
    
    # Register the font in registry
    $FontName = "Yeomil Mono"
    if ($Weight -ne "Regular") {
        $FontName = "Yeomil Mono $Weight"
    }
    # Add (TrueType) suffix
    $FontRegName = "$FontName (TrueType)"
    
    Write-Host "Registering $FontRegName..."
    New-ItemProperty -Path $RegPath -Name $FontRegName -Value $Destination -PropertyType String -Force | Out-Null
}

Write-Host "Yeomil Mono installed successfully! Please restart running applications to use the new fonts."
