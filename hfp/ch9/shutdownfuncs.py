from tkinter import *

from tkinter.messagebox import askokcancel

app = Tk()
app.title("Capturing Events")
app.geometry('250x100+200+200')

def shutdown():
    if askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
        app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()

#Clicking on the close box runs the "shutdown()" function, hich then display an AskOkCancel dialog.
#Add the app.destroy() line of the code to end of your shutdown() function and see if it makes any difference.
