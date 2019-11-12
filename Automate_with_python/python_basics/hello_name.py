#This program says hello and asks for my name

print("Hello there")

print("What is your name?") #ask for their name
myName = input()
print("It's good to meet you, "+ myName)
print("The length of your name is:")
print(len(myName))

print("What is your age?") #Ask for their age
myAge = input()
print("You will be  " + str(int(myAge) + 1) + " in a year.")


"""
--> The excution starts at the top and moves down
--> #Comments are ignored by Python
--> Functions are mini-programs in your program
--> print() displays the value passed to it.
--> input() lets user type in a value
--> len() takes a string value and returns an integer value of the string's length
--> int(), str(), and float() convert values' data type 
"""
