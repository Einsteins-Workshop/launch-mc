@echo off
set username=EinsteinMC_%COMPUTERNAME:~-2%
set pmc=C:\Program Files\Python312\Scripts\portablemc.exe
set mcdir=S:\Minecraft

start "" /min "%pmc%" --work-dir "%mcdir%" --main-dir "%mcdir%" start --username "%username%" 1.19.4
