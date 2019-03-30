#Create a distribution description
#This identifies the module we want setuptools to install.

#Generate a distribution file
#Using Python at the command line, we’ll create a shareable distribution file to contain our module’s code.

# Install the distribution file
#Again, using Python at the command line, install the distribution file (which includes our module) into site-packages.

#Step 1 requires us to create (at a minimum) two descriptive files for our module: setup.py and README.txt.

#vlsearch.py
#setup.py
#README.txt

#Distribution Files ON unix-like OSes

#Execute the code in "setup.py" and pass "sdist" as an argument.
#python3 setup.py sdist

#Installing Pack ages with “pip”
#pip, which is the Package Installer for Python.


#Run Python 3 with the module pip, and then ask pip to install the identified  compressed tar file.
#We are using the "sudo" command here to ensure we install with the correct permissions.
#/dist$ sudo python3 -m pip install vlsearch-1.0.tar.gz
