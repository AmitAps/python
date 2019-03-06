#Import everything from the tkinter module.
from tkinter import *
#Create a tkinter application window called "app".
app = Tk()
#Give the window a name.
app.title("First tkinter application")
#provide window coordinates and size values.
app.geometry('650x300+400+200')

#To add a button to your application, use code like this, being sure to put these two lines of code before the call to mainloop():
#Add a button to the window and give it some text and a width value.
b1 = Button(app, text = "Click me!", width = 10)
#The pack() method links the newly created button to the existing window.
b1.pack(side = 'bottom', padx = 10, pady = 10)
#Start the tkinter event loop.
app.mainloop()
