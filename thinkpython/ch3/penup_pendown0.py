import turtle
window = turtle.Screen()
alex = turtle.Turtle()

alex.pensize(4)

alex.penup()
alex.forward(100)  #This moes alex, but no line is drawn.
alex.shape("turtle")
alex.speed(1)
alex.pendown()
window.mainloop()
