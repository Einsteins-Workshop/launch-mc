import subprocess
import shutil
import os
from win32com.client import Dispatch
#import glob
import sys

def create_shortcut_to_etc_bin(link_name, target, icon_file):
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    #working_directory = "C:\\etc\\bin\\"
    working_directory = "build"
    path = os.path.join(working_directory, link_name)
    icon_file = f"{os.getcwd()}\\build\\assets\\{icon_file}"
    portable_mc_executable = os.path.join(os.path.dirname(sys.executable), "Script", f"{target}.exe")

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = portable_mc_executable
    #shortcut.Targetpath = "cmd.exe"
    #shortcut.arguments = f"/k {target}"
    shortcut.IconLocation = icon_file
    shortcut.save()


subprocess.run(["pip", "install", "portablemc"])
subprocess.run(["pip", "install", "."])

original_path = os.path.join("windows", "etc")
new_path = os.path.join("build")

os.makedirs(new_path, exist_ok=True)

shutil.copytree(original_path, new_path, dirs_exist_ok=True)

#for file in glob.glob(r"C:\etc\bin\*.bat"):
#    print(file)

create_shortcut_to_etc_bin("EW Minecraft.lnk", "launch-1-19-4", "mc-1.19.4.ico")
create_shortcut_to_etc_bin("Code Kingdoms.lnk", "launch-code-kingdoms", "mc-1.16.5.ico")


