#You don't have to put imports at the top of your code, but it is a well-established convention among Python programmers to do so.
from datetime import datetime
import random
import time

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

#The "for" loop iterates EXACTLY five times.
for i in range(5):
    #All of this code is indented under the "for" statement, as it is all part of the "for" statement's suite. Remember: Python does not use curly braces; it uses indentation instead.
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    #The "randint" function provides a random interger that is assigned to a new variable called "wait_time," which.. is then used in the call to "sleep" to pause the program's excecution for a random number of seconds.
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)

#If you simply import a module—for example, import time—you then need to qualify the usage of any of the module’s functions with the module name, like so: time.sleep().
