@echo off
set mcdir=S:\Minecraft

start "" /min "$portable_mc" --work-dir "%mcdir%" --main-dir "%mcdir%" start --username "$user_name" 1.19.4
