#Import the "setup" function from the "setuptools" module.
from setuptools import setup
#This is an invocation of the "setup" function we're spreading its arguments over many lines.
setup(
    #The "name" argument identifies the distribution. It's common practice to name the distribution after the module.
    name='vlsearch',
    version='1.0',
    description='The vowels and letters search tools',
    author_email='amitoct9@@gmail.com',
    url='flyhiee.com',
    #This is a list of ".py" files to include in the package. For this eample, we only have one: "vlsearch"
    py_modules=['vlsearch'],
)
