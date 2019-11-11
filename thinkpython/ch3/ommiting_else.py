import math
x = int(input("Enter the number: "))
if x < 0:
    print("The negative number ", x, " x not valid here.")
    x = 42
    print("I've decided to use the number 42 instead.")

print("The square root of ", x, "is", math.sqrt(x))
