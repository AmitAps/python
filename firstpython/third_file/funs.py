#The function definition starts here
#You need a colon after the function name.
def make_smoothie():
    #The body of the function needs to be indented
    juice = input("What juice would you like? ")
    fruit = input("OK - and how about the fruit? ")
    print("Thanks. Let's go!")
    print("Crushing the ice...")
    print("Blending the " + fruit)
    print("Now adding in the " + juice + " juice")
    print("Finished! There's your " + fruit + " and " + juice + " smoothie!")
#In Python, it’s important that you define the function before you use it, so
#make sure the code that calls (or uses) the function comes after the definition of the function:


#This line isn't indented, because it is part of the main program.
print("Welcome to smoothie-matic 2.0")
another = "Y"
while another == "Y":
    make_smoothie()
    another = input("How about another(Y/N)? ")

#Every time that Python sees make_smoothie() in the code, it jumps
#to the code in the make_smoothie() function. It runs the code in the
#function until it gets to the end, and then returns to the next line in the
#code that called it.
