import turtle
length  = int(input("Enter the length : "))
n_times  = int(input("Enter the n : "))
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

turn = turtle.Turtle()
draw(turn, length, n_times)
