from tkinter import *


app = Tk()
app.title("checkbox")
app.geometry('250x100+200+100')

#Create an "IntVar" to hold a value that is either 1 or 0, depending on whether the checkbox is ticked.
flipper = IntVar()

#The "flip_it()" function is the Checkbutton's event handler.
def flip_it():
    if flipper.get() == 1:
        print("Cool. I'm all ON, man!")
    else:
        print("phooey. I'm OFF.")
#The Checkbutton is asociated with the "IntVar", links to the event handler, and has a descriptive label, too.
Checkbutton(app, variable = flipper, command = flip_it, text = "Flip it?").pack()

app.mainloop()
