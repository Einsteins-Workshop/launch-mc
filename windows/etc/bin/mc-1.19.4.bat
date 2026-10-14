@echo off
set LAST_TWO=%COMPUTERNAME:~-2%
echo %LAST_TWO%| findstr /r "^[0-9][0-9]$" >nul

if %errorlevel% equ 0 (
    :: If they are numbers, keep the last two
    set DIGITS=%LAST_TWO%
) else (
    :: Otherwise, get the first two characters
    set DIGITS=%COMPUTERNAME:~0,2%
)

set username=EinsteinMC_%DIGITS%
set pmc=C:\Program Files\Python312\Scripts\portablemc.exe
set mcdir=S:\Minecraft

start "" /min "%pmc%" --work-dir "%mcdir%" --main-dir "%mcdir%" start --username "%username%" 1.19.4