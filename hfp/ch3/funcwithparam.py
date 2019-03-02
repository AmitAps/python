#A parameter is a value that you send into your function. Think of it as the opposite of what you get when you return a value from a function.
#The parameter’s value works just like a variable within the function, except for the fact that its initial value is set outside the function code:

#To use a parameter in Python, simply put a variable name between the parentheses that come after the definition of the function name and before the colon.
#Then within the function itself, simply use the variable like you would any other:
def shout_out(the_name): #The parameter name goes here.
    return ("Congratulations " + the_name + "!") #Use the parameter's value in your function's code just like any other variable.

#Later, invoke the function from your code with a different parameter value each time you use the function:

print(shout_out('Wanda'))
msg = shout_out('Graham, John, Michael, Eric, and Terry by 2')
print(msg)
print(shout_out('Monty'))


#When a variable's value can be seen by some code, it is said to be “in scope.”
#When a variable's value CANNOT be seen by some code, it is said to be “out of scope.”
