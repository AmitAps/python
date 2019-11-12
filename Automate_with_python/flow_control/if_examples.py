print('Enter a name')
name = input()
#if name:
if name != '':   
    print('Thank you for entering a name')
else:
    print('You did not enter a name.')
"""
Blank string is falsey all others are truthy.

0 is falsey, all others are truthy.
0.0 is falsey, all others are truthy.


An if statement can be used to conditionally execute code, depending on whether or not
the if statement's condition us True or False.

An elif( that is, "else if") statement can follow an if statement. It's block executes if its condition is True and all of the previous conditions have been False.

An else statement comes at the end. It's block is executed if all of the previous conditions have been False.

The values 0, 0.0, and the empty string are considered to be falsey values.
When used in conditions they are considered False. You can always see for yourself which values are Truthly or Falsey  by passing them to the bool() function.
"""
