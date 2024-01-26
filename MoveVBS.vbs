Option Explicit

' Function to execute a PowerShell command
Function ExecutePowerShellCommand(command)
    Dim wshShell, exec, output
    Set wshShell = CreateObject("WScript.Shell")
    Set exec = wshShell.Exec("powershell.exe -command " & command)
    output = exec.StdOut.ReadAll()
    ExecutePowerShellCommand = output
End Function

' Function to simulate random mouse movement using PowerShell
Sub SimulateRandomMouseMovement()
    ' Generate random coordinates (adjust the range based on your screen resolution)
    Dim randomX, randomY
    randomX = Int((1920 - 1 + 1) * Rnd + 1) ' Replace 1920 with your screen width
    randomY = Int((1080 - 1 + 1) * Rnd + 1) ' Replace 1080 with your screen height

    ' Build the PowerShell command with random coordinates
    Dim powershellCommand
    powershellCommand = "[System.Reflection.Assembly]::LoadWithPartialName(""System.Windows.Forms"") | Out-Null; [System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point(" & randomX & ", " & randomY & ")"

    ' Execute the PowerShell command
    ExecutePowerShellCommand(powershellCommand)
End Sub

' Main script
SimulateRandomMouseMovement
