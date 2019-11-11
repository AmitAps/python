import turtle
window = turtle.Screen()
alex = turtle.Turtle()
alex.color('skyblue')
alex.pensize(4)

for i in [0, 1, 2, 3]:
    alex.forward(50)
    alex.left(90)

window.mainloop()
