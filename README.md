# launch-mc
Windows scripts for launching and updating Minecraft clients

The scripts here are specific to our organization's needs. This means
we target our specific Minecraft versions (1.19.4 and 1.16.5 as of 2025-03-27),
and our desktop shortcuts have names and icons that make sense for us.
Please fork and modify the repo as necessary according to your personal preferences.

# Implementation

We use the [portablemc](https://github.com/mindstorm38/portablemc) Python package.

The following steps will be required:

Manual:

0. Start computer in Einstein user

1. Install python.

	a. To check, run cmd in admin mode: type Windows-R, enter `cmd`, and do Shift-Ctl-Enter, typing in admin password

	b. Type `python --version`.  If this gives a python version of 3.12.1 or above, then skip remaining install python
steps
	
    c. If Python 3.12.0a5 is installed, uninstall it with command `winget uninstall python --id Python.Python.3.12` 
       If it shows two options, such as Python3.12.0a5 and Python 3.14.0, run 
       `winget uninstall python --id Python.Python.3.12 --all-versions`

    c. Install python through command line, either `winget install Python.Python.3.13` if no prior version of python
       was installed, or `winget install Python.Python.3.12` if Python 3.12.0a5 was

2. Install git.

	a. To check, run `git --version`.  If this gives any sort of version, then skip remaining install git steps

	b. Install git through command line call `winget install git --id Git.Git --source winget`

3. Clone repository

    a. In any writeable directory (preferrably in C:\Users\Einstein), run 
    `git clone https://github.com/Einsteins-Workshop/launch-mc.git`

4. In command prompt, type `echo %COMPUTERNAME%` to check that %COMPUTERNAME% has the correct format, either starting 
with EINSTEIN and ending in two digits or starting with some number of digits. If not, report to IT

5. Make sure that Minecraft is already installed on the computer

6. If using a windows machine, go to repository in a command shell that is run as admininstrator and 
    a. Run `pip install pywin32`
    b. Run `python windows_setup.py` while in the git clone directory

7. Copy shortcuts from the subdirectory build in the launch-mc subdirectory to the Desktop

8. Pin the 1.19.4 Minecraft launcher to the taskbar.



The script should do the following:

1. Install portablemc
2. Move files to launch-mc\build directory
3. Create shortcuts


After setup, make sure to run mc-update.bat to start update process
