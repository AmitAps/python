spam = 42 # global variable

def eggs():
    spam = 42 #local variable


print('Some code here')
print('some more code')

"""
Code in the global scope cannot use any local variables.

Code in a local scope can access global variable.

Code in one function's local scope cannot use variables in another local scope.

Code in one function's local scope cannot use variables in any other local scope.
"""
