@echo off
set email=itaccounts_%COMPUTERNAME:~-2%@einsteinsworkshop.com
set pmc=C:\Program Files\Python312\Scripts\portablemc.exe
set mcdir=S:\Minecraft

start "" /min "%pmc%" --work-dir "%mcdir%" --main-dir "%mcdir%" start --login "%email%" 1.16.5
