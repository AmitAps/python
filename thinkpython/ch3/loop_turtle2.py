import turtle
window = turtle.Screen()
alex = turtle.Turtle()

alex.pensize(4)

for color in ["yellow", "red", "purple", "blue"]:
    alex.color(color)
    alex.forward(50)
    alex.left(90)

window.mainloop()
