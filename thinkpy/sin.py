import math
degrees = float(input("Enter degrees in Float:"))
x = math.sin(degrees / 360.0 * 2 * math.pi)
print(f"the value of sin {degrees} is {x}" )
