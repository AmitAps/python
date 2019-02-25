import turtle

n = int(input("Enter number of side for draw: "))
length = float(input("Enter length of side for draw: "))
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

bob = turtle.Turtle()    
polygon(bob, n, length)
