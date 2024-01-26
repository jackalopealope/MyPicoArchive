@echo off
setlocal EnableDelayedExpansion

REM Check if the -v flag is passed
set "verbose="
if "%~1" == "-v" set "verbose=true"

:start

REM Generate random X and Y coordinates
set /a "randomX=!random! %% 1366"  REM Replace 1366 with your screen width
set /a "randomY=!random! %% 768"  REM Replace 768 with your screen height

REM Execute the PowerShell command to set the mouse cursor position
powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point(!randomX!, !randomY!)"

REM Optional: Display the randomly generated coordinates only if -v flag is passed
if defined verbose (
    echo Mouse moved to X=!randomX!, Y=!randomY!
)

timeout >nul /nobreak /t 1  REM Shortest possible delay (1 millisecond)

goto start

endlocal
