import turtle
window = turtle.Screen()
alex = turtle.Turtle()

alex.pensize(4)

# Assign a list to a variable
colors = ["yellow", "red", "purple", "blue"]
for color in colors:
    alex.color(color)
    alex.forward(50)
    alex.left(90)

window.mainloop()
