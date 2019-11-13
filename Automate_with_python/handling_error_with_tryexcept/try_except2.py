print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')


"""
A devide-by-zero error happens when Python divides a number by zero.

Errors cause the program to crash.

An error that happens inside a try block will cause code in the except block to execute.
That code can handle the error or display a message to the user so that the program can keep going.
"""
