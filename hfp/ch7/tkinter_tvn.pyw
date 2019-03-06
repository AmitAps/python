#Import everything from the tkinter module.
from tkinter import *
#Create a tkinter application window called "app".
app = Tk()
def button_click():
    print("I've just been clicked!")
#Give the window a name.
app.title("First tkinter application")
#provide window coordinates and size values.
app.geometry('650x300+400+200')
#Create a button for the “Correct" event
b1 = Button(app, text="Correct", width = 10, command = button_click)
b1.pack(side='left', padx = 10, pady = 10)
#Create a button for the “Wrong" event
b2 = Button(app, text="Wrong", width = 10)
b2.pack(side='right', padx = 10, pady = 10)

app.mainloop()
