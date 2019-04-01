#Import the function.
from flask import escape

#Use "escape" with a normal string.
print(escape('This is a Request'))

#Use "escape" with a string containing some special characters.
print(escape('This is a <Request>'))