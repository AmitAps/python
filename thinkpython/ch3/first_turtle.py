import turtle  #Allows us to use turtles
window = turtle.Screen() #Create a playground for turtles
amit = turtle.Turtle()  #Create a turtle, assin to amit

amit.color('red')
amit.forward(50)  #Tell amit to move forward by 50 units
amit.left(90)     #Tell amit to turn by 90 degrees
amit.forward(30)  #Complete the second side of a rectangle

window.mainloop()  #Wait for user to close window
