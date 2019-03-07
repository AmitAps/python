#Import tkinter
from tkinter import *
#Define a function save_data
def save_data():
    #Appened the text to the end of the file.
    fileD = open("deliveries.txt", "a")
    fileD.write("Depot:\n")
    #get() returns the contents of an Entry field.
    fileD.write("%s\n" % depot.get())
    fileD.write("Description:\n")
    fileD.write("%s\n" % description.get())
    fileD.write("Address\n")
    #get("1.0", END) returns the contents of a Text field
                                      #This means "1st row, 0th column." Remember that rows start at 1 and columns from 0.
    fileD.write("%s\n" % address.get("1.0", END))
    fileD.write("------------------------------------------------------:\n")

    #Don't forget to clear the fields after saving the data
    depot.delete(0, END)
    description.delete(0, END)
    address.delete("1.0", END)


#Create the GUI
app = Tk()




#Give name to the GUI
app.title("Head-Ex Deliveries")
#You don't need to keep track of the labels, so no need to assign them to variable.
#Recall thet "pack()" adds the widgets to the window.
#Calling "pack()" without options means you leave it to tkinter to decide how best to lay things out on the GUI.
Label(app, text = "Depot:").pack()

#A StringVar is just like the IntVar from chapter 7, except that it holds a string value.
#This sets the StringVar to the special value.
depot = StringVar()
#"None" which means "No Value".
depot.set(None)
#You don't need the Entry field anymore.
#The text is the description that appears on the screen.
#This VALUE is the one that will be used in the model.
#You can make the text diferent from the value, but let's leave them the same here.
Radiobutton(app, text = "Cambridge, MA", value = "Cambridge, MA", variable = depot).pack()
Radiobutton(app, text = "Cambridge, UK", value = "Cambridge, UK", variable = depot).pack()
Radiobutton(app, text = "Seattle, WA", value = "Seattle, WA", variable = depot).pack()
#Create two fields: one is an Entry field and the other is a Text field.
#Don't forget to pack those widgets.
Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()
#Address is a larger Text field.
Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()
app.mainloop()
