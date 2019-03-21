
#Import the module you need, then access the attribute of interest.
import sys
import os
print(sys.platform) #This will print the kernel name of system.

#This will print the which version of Python is running.
print(sys.version)

print(os.getcwd())
#The "environ" attribute contains lots of data.
print(os.environ)

#You can access a specifically named attribute(from the data contained in "environ") using "getenv".
print(os.getenv('HOME'))
