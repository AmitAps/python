from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

#Here's another variable being created and asigned a value.
#This call generates a value to assign to the variable.
right_this_minute = datetime.today().minute
#OR
#First determine the current time ...
#time_now = datetime.today()
#right_this_minute = time_now.minute #..then extract the minute value.

#The in operator checks if one thing is inside another.
#This "if" statement will evaluate to either "True" or "False".
if right_this_minute in odds:
    #The "print" function display a message on standard output(i.e, your screen).
    #Here is one block of code Note: the code is indented.
    print("This minute seems a little odd.")
else:
    #And here is another block of code. Note: It's indented , too.
    print("Not an odd minute.")
