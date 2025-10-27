import subprocess
import shutil
import os
from win32com.client import Dispatch
import glob

def create_shortcut_to_etc_bin(link_name, bat_file, icon_file):
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    path = os.path.join(desktop, link_name)
    working_directory = "C:\\etc\\bin\\"
    path = os.path.join(working_directory, link_name)
    target = working_directory + bat_file
    icon_file = working_directory + icon_file

    print(path)
    print(target)
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = working_directory
    shortcut.IconLocation = icon_file
    shortcut.save()


subprocess.run(["pip", "install", "portablemc"])

original_path = os.path.join("windows", "etc")
new_path = os.path.join("C:", os.sep, "etc")

os.makedirs(new_path, exist_ok=True)

shutil.copytree(original_path, new_path, dirs_exist_ok=True)

for file in glob.glob(r"C:\etc\bin\*.bat"):
    print(file)

create_shortcut_to_etc_bin("Minecraft_1.19.4.lnk", "mc-1.19.4.bat", "mc-1.19.4.ico")
create_shortcut_to_etc_bin("Minecraft Code Kingdoms.lnk", "mc-codekingdoms.bat", "mc-1.16.5.ico")


