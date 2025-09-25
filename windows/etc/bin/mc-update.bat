@echo off
set mcdir=S:\Minecraft
set pmc=C:\Program Files\Python312\Scripts\portablemc.exe
set psx=C:\Program Files\WinGet\Links\psexec.exe

@REM Update specific MC versions
@REM "%psx%" -accepteula -nobanner -d -i 1 -u "Einstein" -p "" "%pmc%" --work-dir "%mcdir%" --main-dir "%mcdir%" start --dry --username "%username%" 1.19.4
@REM "%psx%" -accepteula -nobanner -d -i 1 -u "Einstein" -p "" "%pmc%" --work-dir "%mcdir%" --main-dir "%mcdir%" start --dry --username "%username%" 1.16.5
"%pmc%" --work-dir "%mcdir%" --main-dir "%mcdir%" start --dry 1.19.4
"%pmc%" --work-dir "%mcdir%" --main-dir "%mcdir%" start --dry 1.16.5

@REM Don't know of a universal way to start Minecraft Launcher regardless of direct install or
@REM Windows Store. So we'll try a few different methods.

@REM 1. Launch MC Launcher executable directly
set location1=C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe

@REM 2. & 3. Launch MC Launcher using the start menu shortcut.
set shortcut_path=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Minecraft Launcher\Minecraft Launcher.lnk
for /f "delims=" %%a in ('wmic path win32_shortcutfile where "name='%shortcut_path:\=\\%'" get target /value') do (
for /f "tokens=2 delims==" %%b in ("%%~a") do (
  set target_path=%%~b
  )
)
set "location2=%target_path%"

set shortcut_path=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Minecraft Launcher.lnk
for /f "delims=" %%a in ('wmic path win32_shortcutfile where "name='%shortcut_path:\=\\%'" get target /value') do (
for /f "tokens=2 delims==" %%b in ("%%~a") do (
  set target_path=%%~b
  )
)
set "location3=%target_path%"

@REM 4. Launch MC Launcher using desktop shortcut

set shortcut_path=C:\Users\Einstein\Desktop\Minecraft Launcher.lnk
for /f "delims=" %%a in ('wmic path win32_shortcutfile where "name='%shortcut_path:\=\\%'" get target /value') do (
for /f "tokens=2 delims==" %%b in ("%%~a") do (
  set target_path=%%~b
  )
)
set "location4=%target_path%"

set shortcut_path=C:\Users\Public\Desktop\Minecraft Launcher.lnk
for /f "delims=" %%a in ('wmic path win32_shortcutfile where "name='%shortcut_path:\=\\%'" get target /value') do (
for /f "tokens=2 delims==" %%b in ("%%~a") do (
  set target_path=%%~b
  )
)
set "location5=%target_path%"

if        exist "%location1%" ( set "location=%location1%"
) else if exist "%location2%" ( set "location=%location2%"
) else if exist "%location3%" ( set "location=%location3%"
) else if exist "%location4%" ( set "location=%location4%"
) else if exist "%location5%" ( set "location=%location5%"
)

if exist "%location%" (
  "%psx%" -accepteula -nobanner -d -i 1 -u "Einstein" -p "" "%location%"
  timeout /t 600
  FOR /F "delims=" %%I in ("%location%") do taskkill /im %%~nxI /f
)
