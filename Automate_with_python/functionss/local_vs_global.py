def spam():
    #eggs = 99 #local variable
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)
"""
Assignment statement = Local variable

No assignment statement = Global variable


A scope can be thought of as an area of the source code, and as a container of variables.

The global scope is code outside of all functions. Variables assigned here are global variables.

Each function's code is in its own local scope. Variables assigned here are local variables.

Code in the global scope cannot use any local variables.

Code in a function's local scope cannot use variables in any another function's local scope.

If there's an assignment statement for a varible in a function, that is a local variable.
"""
