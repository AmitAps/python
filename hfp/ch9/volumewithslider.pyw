from tkinter import *
import pygame.mixer
from time import sleep

#Create the GUI application window.
app = Tk()
app.title("Head first mix")

mixer = pygame.mixer
mixer.init()

track = mixer.Sound("50459_M_RED_Nephlimizer.wav")
print("play it LOUD, man!")
track.play(loops = -1)

#Set the volume to a LOUD setting.
track.set_volume(0.9)
sleep(2)
print("Softly does it ...")

#Set the volume to a very low setting.
track.set_volume(0.1)
sleep(2)
track.stop()

volume = DoubleVar()
volume_scale = Scale(app, variable = volume, from_ = 0.0, resolution = 0.1, command = change_volume, label = "Volume", orient = HORIZONTAL)
volume_scale.pack(side = RIGHT)
app.mainloop()
