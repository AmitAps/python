import turtle
import math
radius = int(input("Enter radius for the circle: "))
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        

    
def arc(t, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = float(angle) / n
        polyline(t, n, step_length, step_angle)
        
def circle(t, r):
    arc(t, r, 360)



bob = turtle.Turtle()
circle(bob, radius)
