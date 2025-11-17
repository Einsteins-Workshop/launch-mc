import os
import re
import shutil
import subprocess

def launch_1_19_4():
    app_dir = app_directory()
    return subprocess.run(
        [
            find_portablemc(),
            "--work-dir",
            app_dir,
            "--main-dir",
            app_dir,
            "start",
            "--username",
            user_name(),
            "1.19.4"
        ],
        shell=True,
        capture_output=True,
        text=True
    )

def launch_code_kingdoms():
    app_dir = app_directory()

    return subprocess.run(
        [
            find_portablemc(),
            "--work-dir",
            app_dir,
            "--main-dir",
            app_dir,
            "start",
            "--login",
            user_email(),
            "1.16.5"
        ],
        shell=True,
        capture_output=True,
        text=True
    )

def find_python_directory():
    return os.path.dirname(shutil.which("python"))

def find_portablemc():
    python_directory = find_python_directory()
    portablemc = os.path.join(python_directory, "Scripts", "portablemc.exe")
    if os.path.exists(portablemc):
        return portablemc
    raise FileNotFoundError(f"Could not find portablemc.exe in {python_directory}")

def computer_number():
    computer_name = os.environ["COMPUTERNAME"]
    result = re.search(r'Einstein.*(\d+)$', computer_name)
    if result == None:
        result = re.search(r'^(\d+)', computer_name)

    if result == None and computer_name == "BOOKKEEPER":
        return "01"

    if result == None:
        raise RuntimeError(f"Could not find computer number from {computer_name}")
    else:
        return result.group(0)

def user_name():
    return f"EinsteinMC_{computer_number()}"

def user_email():
    return f"itaccounts_{computer_number()}@einsteinsworkshop.com"

def app_directory():
    if os.path.exists('s:\\'):
        return ('s:\\minecraft')
    if os.path.exists('c:\\etc\\bin'):
        return ('c:\\etc\\bin\\minecraft')
    raise FileNotFoundError("Could not find an app directory in either s: or c:\etc\bin.")