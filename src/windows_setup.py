import subprocess
import shutil
import os
from win32com.client import Dispatch
from minecraft_launcher.launcher import user_name, find_portablemc, computer_number
from string import Template
import sys

def create_shortcut_to_etc_bin(link_name, target, icon_file):
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    working_directory = "build"
    path = os.path.join(working_directory, link_name)
    icon_file = f"{os.getcwd()}\\build\\assets\\{icon_file}"

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = icon_file
    shortcut.save()

def python_executable(target):
    return os.path.join(os.path.dirname(sys.executable), "Scripts", f"{target}.exe")

try:
    computer_number()
except RuntimeError as err:
    print(err)
    print("Contact IT if you find this error.")
    exit()

# Check if python excecutable is appropriate
python_path = os.path.dirname(sys.executable)
if not(python_path.startswith("C:\\Program Files")):
    print(f"The python installation that you are using, {python_path}, is not associated with the system.")
    print("Make sure to run with admin privileges.")
    exit()


os.chdir("..")
subprocess.run(["pip", "install", "portablemc"])

new_path = os.path.join("build")
os.makedirs(new_path, exist_ok=True)
original_path = os.path.join("windows", "etc")
shutil.copytree(original_path, new_path, dirs_exist_ok=True)

try:
    subprocess.run(["pip", "install", "."], check=True)
    create_shortcut_to_etc_bin("EW Minecraft.lnk", "launch-1-19-4", "mc-1.19.4.ico")
    create_shortcut_to_etc_bin("Code Kingdoms.lnk", "launch-code-kingdoms", "mc-1.16.5.ico")
except subprocess.CalledProcessError:
    print("Failed to install python file")
    # Use our backup plan to install templated .bat file
    context = {
        'user_name': user_name(),
        'portable_mc': str(find_portablemc())
    }

    batch_file = "mc-1.19.4.bat"
    with open(os.path.join("windows", "template", batch_file)) as template:
        batch_file_template = Template(template.read())
        batch_file_string = batch_file_template.substitute(context)

        os.makedirs(new_path, exist_ok=True)
        with open(os.path.join("build", batch_file), "w") as file_to_write:
            file_to_write.write(batch_file_string)

        batch_file_path = f"{os.getcwd()}\\build\\{batch_file}"
        create_shortcut_to_etc_bin("EW Minecraft.lnk", batch_file_path, "mc-1.19.4.ico")
        print("Backup installation method successful, ignore errors with metadata-generation-failed")
