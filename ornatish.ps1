# Montaj tizimi o'rnatuvchisi (Windows 10/11, x64). Ishga tushirish: ornatish.cmd ni ikki marta bosing
# (yoki PowerShell'da:  powershell -ExecutionPolicy Bypass -File ornatish.ps1).
# Nima qiladi: dasturlar (winget: Python, Node, ffmpeg, Git, yt-dlp) + whisper.cpp -> %USERPROFILE%\VideoMontaj
#              -> model (GitHub Release'dan) -> Mixkit -> Claude skill'lari -> HyperFrames brauzeri.
# Tashqi dasturlar (npx, winget) stderr'ga yozsa PowerShell 5.1 "Stop" rejimida to'xtab qoladi - shuning uchun
# ular uchun Continue, ularning natijasi $LASTEXITCODE bilan tekshiriladi; PowerShell buyruqlari esa xatoda to'xtaydi.
$ErrorActionPreference = "Continue"
$PSDefaultParameterValues["*:ErrorAction"] = "Stop"
$ProgressPreference = "SilentlyContinue"
$Manba = Split-Path -Parent $MyInvocation.MyCommand.Path
$VM = Join-Path $env:USERPROFILE "VideoMontaj"
$WhisperUrl = "https://github.com/ggml-org/whisper.cpp/releases/download/b5130/whisper-bin-x64.zip"
$HF = "hyperframes@0.8.134"
$ModelUrl = "https://github.com/asositgroup/montaj-claude/releases/download/model-v1/ggml-rubaistt.bin"
$ModelSha = "1B02DF434902015E1464611A7748927E42FCB55C49791C85239CF713C8EDC1A3"
$Tar = Join-Path $env:SystemRoot "System32\tar.exe"   # Git'ning GNU tar'i C:\ yo'llarini noto'g'ri tushunadi

function Qadam($m) { Write-Host ""; Write-Host ">> $m" -ForegroundColor Cyan }
function Ok($m) { Write-Host "  [OK] $m" -ForegroundColor Green }
function Xato($m) { Write-Host "[XATO] $m" -ForegroundColor Red; exit 1 }
function Yangila-Path {
  $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [Environment]::GetEnvironmentVariable("Path", "User")
}
function Bor($cmd) { [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function Python-Ishlaydimi {
  # Microsoft Store'ning "python" yorlig'i haqiqiy Python emas - tekshirib ko'ramiz
  try { $v = & python -c "print(42)" 2>$null; return ($v -eq "42") } catch { return $false }
}
function Winget-Ornat($id) {
  winget.exe install --id $id -e --silent --accept-package-agreements --accept-source-agreements --disable-interactivity | Out-Host
  Yangila-Path
}

Qadam "Tizim"
if (-not [Environment]::Is64BitOperatingSystem) { Xato "64-bitli Windows kerak." }
if ($env:PROCESSOR_ARCHITECTURE -eq "ARM64") { Write-Host "  Diqqat: ARM kompyuter - ishlashi mumkin, lekin x64 (Intel/AMD) tavsiya." }
Ok "Windows $([Environment]::OSVersion.Version)"

Qadam "Dasturlar (winget)"
$kerak = @(
  @{ id = "Python.Python.3.12"; bor = { Python-Ishlaydimi }; nom = "Python" },
  @{ id = "OpenJS.NodeJS.LTS"; bor = { Bor "node" }; nom = "Node.js" },
  @{ id = "Gyan.FFmpeg"; bor = { Bor "ffmpeg" }; nom = "ffmpeg" },
  @{ id = "Git.Git"; bor = { Bor "git" }; nom = "Git (Claude Code uchun)" },
  @{ id = "yt-dlp.yt-dlp"; bor = { Bor "yt-dlp" }; nom = "yt-dlp" }
)
foreach ($p in $kerak) {
  if (& $p.bor) { Ok $p.nom; continue }
  if (-not (Bor "winget")) { Xato "winget yo'q. Microsoft Store'dan 'App Installer' ni o'rnating va qayta ishga tushiring." }
  Write-Host "  ... $($p.nom) o'rnatilmoqda"
  Winget-Ornat $p.id
  if (-not (& $p.bor)) { Xato "$($p.nom) o'rnatilmadi. Kompyuterni qayta yoqib, skriptni yana ishga tushiring." }
  Ok $p.nom
}
& python -m pip install --user --quiet --disable-pip-version-check gallery-dl
Ok "gallery-dl"

# Python matn fayllarini UTF-8 da o'qisin (o'zbekcha belgilar); Claude ochgan yangi terminallar uchun ham
[Environment]::SetEnvironmentVariable("PYTHONUTF8", "1", "User"); $env:PYTHONUTF8 = "1"

Qadam "%USERPROFILE%\VideoMontaj"
New-Item -ItemType Directory -Force -Path $VM | Out-Null
# kod yangilanadi; o'z ishlaringiz (ish\, videos\) o'chirilmaydi; o'zingiz tuzatgan STYLE.md ustidan yozilmaydi
robocopy "$Manba\VideoMontaj" $VM /E /XD "$Manba\VideoMontaj\styles" /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { Xato "Nusxalashda xato (robocopy $LASTEXITCODE)." }
robocopy "$Manba\VideoMontaj\styles" "$VM\styles" /E /XC /XN /XO /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { Xato "Uslublarni nusxalashda xato (robocopy $LASTEXITCODE)." }
$global:LASTEXITCODE = 0
Ok $VM

Qadam "whisper.cpp (nutqni matnga)"
$WDir = Join-Path $VM "bin\whisper"
$WCli = Get-ChildItem -Path $WDir -Recurse -Filter "whisper-cli.exe" -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $WCli) {
  New-Item -ItemType Directory -Force -Path $WDir | Out-Null
  $zip = Join-Path $env:TEMP "whisper-bin-x64.zip"
  Invoke-WebRequest -Uri $WhisperUrl -OutFile $zip
  Expand-Archive -Path $zip -DestinationPath $WDir -Force
  Remove-Item $zip
  $WCli = Get-ChildItem -Path $WDir -Recurse -Filter "whisper-cli.exe" | Select-Object -First 1
}
if (-not $WCli) { Xato "whisper-cli.exe topilmadi." }
[Environment]::SetEnvironmentVariable("MONTAJ_WHISPER", $WCli.FullName, "User"); $env:MONTAJ_WHISPER = $WCli.FullName
Ok $WCli.FullName

Qadam "Model va namunalar"
$Model = Join-Path $VM "modellar\ggml-rubaistt.bin"
if (-not (Test-Path $Model)) {
  Write-Host "  ... model yuklanmoqda (823 MB, bir marta)"
  New-Item -ItemType Directory -Force -Path (Split-Path $Model) | Out-Null
  $Vaqt = "$Model.yuklanmoqda"
  Invoke-WebRequest -Uri $ModelUrl -OutFile $Vaqt
  if ((Get-FileHash -Algorithm SHA256 $Vaqt).Hash -ne $ModelSha) { Remove-Item $Vaqt; Xato "Model fayli buzilgan (sha256 mos emas)." }
  Move-Item $Vaqt $Model
}
if (-not (Test-Path "$VM\videos\c0038-500-dollar")) { Xato "Namuna yo'q (repo to'liq emas)." }
Ok "model, namuna"

Qadam "Ovoz effektlari va musiqa (Mixkit, bepul litsenziya)"
& python "$VM\vosita\mixkit.py"
if ($LASTEXITCODE -ne 0) { Xato "Mixkit fayllari yuklanmadi." }
# namuna loyihaning SFX va musiqasi ham Mixkit'dan (repoda tarqatilmaydi); video.mp4 - o'zingizniki
$N = "$VM\videos\c0038-500-dollar\assets"
New-Item -ItemType Directory -Force -Path "$N\sfx" | Out-Null
foreach ($f in "whoosh_pop","click","sweep","tugma","pop","sehr","ding","tanga","whoosh_tez","zarba","pop_quruq","yozish") {
  if (-not (Test-Path "$N\sfx\$f.mp3")) { Copy-Item "$VM\assets\ovoz\$f.mp3" "$N\sfx\" }
}
if (-not (Test-Path "$N\musiqa.mp3")) { Invoke-WebRequest -Uri "https://assets.mixkit.co/music/126/126.mp3" -OutFile "$N\musiqa.mp3" }
Ok "namuna loyiha SFX + musiqa"

Qadam "Claude skill'lari -> %USERPROFILE%\.claude\skills"
$S = Join-Path $env:USERPROFILE ".claude\skills"
New-Item -ItemType Directory -Force -Path $S | Out-Null
$Zaxira = Join-Path $env:USERPROFILE (".claude\skills-zaxira-" + (Get-Date -Format "yyyyMMdd-HHmmss"))
foreach ($d in Get-ChildItem -Directory "$Manba\skills") {
  $m = Join-Path $S $d.Name
  if (Test-Path $m) { New-Item -ItemType Directory -Force -Path $Zaxira | Out-Null; Move-Item $m $Zaxira }
  Copy-Item -Recurse $d.FullName $m
  Ok $d.Name
}
if (Test-Path $Zaxira) { Write-Host "  (eski nusxalar: $Zaxira)" }
# HyperFrames skill'lari (hyperframes*, media-use, general-video, talking-head-recut) - rasmiy CLI, eng yangi versiya
& npx --yes hyperframes@latest skills update general-video talking-head-recut
if ($LASTEXITCODE -ne 0) { Xato "HyperFrames skill'lari o'rnatilmadi." }
Ok "HyperFrames skill'lari"

Qadam "HyperFrames brauzeri"
Push-Location "$VM\videos\c0038-500-dollar"
& npx --yes $HF browser ensure | Out-Null
if ($LASTEXITCODE -ne 0) { Pop-Location; Xato "HyperFrames brauzeri o'rnatilmadi." }
Ok "brauzer"

Qadam "Tekshiruv"
& npx --yes $HF check *> $null
if ($LASTEXITCODE -eq 0) { Ok "namuna loyiha tekshiruvdan o'tdi" } else { Write-Host "  Diqqat: namuna tekshiruvi ogohlantirish berdi (npx hyperframes check)" }
Pop-Location
Write-Host ""
Write-Host "TAYYOR. Yangi terminal oching, Claude Code'ni ishga tushiring va yozing:  /montaj <video yo'li>   (README.md da batafsil)" -ForegroundColor Green

exit 0
