import math

radius = float(input("Enter the radius of a cirlce: "))

def area(radius):
    a = math.pi * radius**2
    return a

area_of_circle = area(radius)
print(f'Area of circle is {area_of_circle}')
