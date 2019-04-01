#This is the module's name "flask" with a lowercase "f".
#This is the class name "Flask" with an uppercase "F".

#The second line of code creates an object of type Flask, assigning it to the app variable.

from flask import Flask
#Create an instance of a Flask object and assign it to "app".
#The __name__ value is maintained by the Python interpreter and, when used anywhere within your program’s code, is set to the name of the currently
#active module. It turns out that the Flask class needs to know the current value of __name__ when creating a new Flask object, so it must be
#passed as an argument, which is why we’ve used it here (even though its usage does look strange).
app = Flask(__name__)
#A function decorator adusts the behavior of an existing function (without changing the function's code).
#Here's the function decorator, hich -like all decorators-is prefixed with @ symbol.
            #this is the URL.
@app.route('/')
#This is just a regular Python function which, when invoked, returns a string to its caller (note the '->str' annotation).
def hello() ->str:
    return 'Hello world from Flask!'

#Asks the webapp to start running.
app.run()