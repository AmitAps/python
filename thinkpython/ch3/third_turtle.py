import turtle
color_name = input("Enter the background color for window: ")
pen_color = input("Enter the pen color : ")
window = turtle.Screen()
window.bgcolor("%s" % str(color_name))  #Set the window background color
window.title('Hello, Tess!')  #Set the window title

tess = turtle.Turtle()
tess.color("%s" % str(pen_color))            #Tell tess to change her color
tess.pensize(3)               #Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

window.mainloop()
