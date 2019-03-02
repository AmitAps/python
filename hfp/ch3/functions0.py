#A function is a chunck of code that you separate out from the rest of your program, give a name, and then call from your code.
#A function is a boxed-up piece of reusable code.
#In python use the def keyword to define a function.
def make_smoothie(): #Give function a name. The parentheses are important, so be sure to include them.
    juice = input("What juice would you like? ")
    fruit = input("OK - and how about the fruit? ")
    #The code you share is indented.
    print("Thanks. Let's go!")
    print("Crushing the ice...")
    print("Blending the " + fruit)
    print("Now adding in the " + juice + " juice")
    print("Finished! There's your " + fruit + " and " + juice + " smoothie!")

#In Python, it’s important that you define the function before you use it, so
#make sure the code that calls (or uses) the function comes after the definition of the function:
print("Welcome to smoothie-matic 2.0")
another = "Y"
while another == "Y":
    make_smoothie() #Call the function . Note the use of parens.
    #When the cmputer first encounters a call to the function, it jumps to the start of the code
    #function, runs the code it finds there... then returns to the calling piece of code.
    #The function "answers the call" to run its code.
    another = input("How about another(Y/N)? ")
