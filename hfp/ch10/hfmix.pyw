from tkinter import *
from sound_panel import *
from tkinter.messagebox import askokcancel

import pygame.mixer



app = Tk()
app.title("Head first mix")

mixer = pygame.mixer
mixer.init()

create_gui(app, mixer, "50459_M_RED_Nephlimizer.wav")
create_gui(app, mixer, "49119_M_RED_HardBouncer.wav")

def shutdown():
    if askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
        app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
