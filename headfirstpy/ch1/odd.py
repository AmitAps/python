#Think of modules as a collection of related functions.
        #This is the name of the standard library module to import the reusable code from.
#Remember: the interpreter starts at the top of the file and works down toward the bottom, excuting each line of Python code as it goes.
from datetime import datetime #This is the name of the submodule.

#This is a new variable, called "odds", which is assigned a list of odd numbers.
        #This is the list of odd numbers, enclosed in the square brackets.
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
#Like arrays , lists can hold data of any type.

right_this_minute = datetime.today().minute

if right_this_minute in odds: #Colons introduce indented suites.
    print("This minutes seems a little odd.")
else: #Colons introduce indented suites.
    print("Nou ot an odd minute.")

#The colon (:) is important, in that it introduces a new suite of code that must be indented to the right. If you forget to indent your code after a colon, the interpreter raises an error.

#Instead of referring to a code "block," Python programmers use the word "suite." Both names are used in practice but the python docs prefer "suite."
