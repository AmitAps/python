#Import tkinter
from tkinter import *

#Define a function save_data
def save_data():
    #Appened the text to the end of the file.
    fileD = open("deliveries_final.txt", "a")
    fileD.write("Depot:\n")
    #get() returns the contents of an Entry field.
    fileD.write("%s\n" % depot.get())
    fileD.write("________________\n")
    fileD.write("Description:\n")
    fileD.write("%s\n" % description.get())
    fileD.write("________________\n")
    fileD.write("Address\n")
    #get("1.0", END) returns the contents of a Text field
                                      #This means "1st row, 0th column." Remember that rows start at 1 and columns from 0.
    fileD.write("%s\n" % address.get("1.0", END))
    fileD.write("------------------------------------------------------:\n")

    #Don't forget to clear the fields after saving the data
    depot.set(None)
    description.delete(0, END)
    address.delete("1.0", END)

def read_depots(file):
    #Start with an empty array
    depots = []
    #Open the file
    depots_f = open(file)
    #Read from the file one line at a time.
    for line in depots_f:
        #When you read a line from the file, it might have a newline character at the end. The rstrip() string method will remove it for you.
        depots.append(line.rstrip())
    #Return the list to the calling code.
    return depots

#Create the GUI
app = Tk()


app.configure(background='#00bfff')

#Give name to the GUI
app.title("Head-Ex Deliveries")
#You don't need to keep track of the labels, so no need to assign them to variable.
#Recall thet "pack()" adds the widgets to the window.
#Calling "pack()" without options means you leave it to tkinter to decide how best to lay things out on the GUI.
Label(app, text = "Depot:", font=('Verdana', 16, 'bold'), bg="skyblue").pack(padx=5, pady=5)

#A StringVar is just like the IntVar from chapter 7, except that it holds a string value.
#This sets the StringVar to the special value.
depot = StringVar()
#"None" which means "No Value".
depot.set(None)

#Call the function, passing in the name of the file to read the data from.
options = read_depots("depots.txt")
#This * means "Take the rest of the parameter from this list and insert them here."
#Use the data to build  the option menu.
OptionMenu(app, depot, *options).pack(padx=5, pady=5)

#Create two fields: one is an Entry field and the other is a Text field.
#Don't forget to pack those widgets.
Label(app, text = "Description:", font=('Verdana', 16, 'bold'), bg="skyblue").pack(padx=5, pady=5)
description = Entry(app)
description.pack()
#Address is a larger Text field.
Label(app, text = "Address:", font=('Verdana', 16, 'bold'), bg="skyblue").pack(padx=5, pady=5)
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data, font=('Verdana', 16, 'bold'), bg="skyblue").pack(padx=15, pady=10)
app.mainloop()
