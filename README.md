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

1. Install python.
	a. To check, run cmd to bring up cmd prompt
	b. Type python --version.  If this gives a python version of 3.0 or above, then skip remaining install python steps
	c. Go to python.org/downloads and click on "Download Python install manager"

2. Install git.
	a. To check, run git --version.  If this gives any sort of version, then skip remaining install git steps
	b. Go to git-scm.com/install and install git

3. Clone repository
	a. In any writeable directory, run git clone https://github.com/Einsteins-Workshop/launch-mc.git

4. In command prompt, check that %COMPUTERNAME% has the correct format, either starting with EINSTEIN and ending in two digits or starting with some number of digits. If not, report to IT

5. Make sure that Minecraft is already installed on the computer

6. If using a windows machine, go to repository in a command shell that is run as admininstrator and 
    a. Run pip install pywin32
    b. Run python windows_setup.py

7. Copy shortcuts from this directory, launch-mc\build to Desktop



The script should do the following:

1. Install portablemc
2. Move files to launch-mc\build directory
3. Create shortcuts


After setup, make sure to run mc-update.bat to start update process
