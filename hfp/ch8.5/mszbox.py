import tkinter.messagebox
                            #The title of the message box.
tkinter.messagebox.showinfo("Delivery", "The cupcakes have arrived in Istanbul")
                                        #The content of the message.
#f you need a message box that asks the users a question, you will need to check the return value to see what they chose:
response = tkinter.messagebox.askyesnocancel("Gift?", "Gift wrap the package?")
#A value is assigned to “response” after the user clicks one of the buttons.
#When tkinter gets to this line, it will wait for the user to answer the question and then assign True (yes), False (no), or None (cancel) to the response variable.
