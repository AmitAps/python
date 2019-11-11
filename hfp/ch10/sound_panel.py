#Begin by importing the libraries you need to use in this module.
from tkinter import *
import pygame

#Create a new function that contains the GUI-creating code from the current program.
#Note: when this function is called it is expecting three parameters.
def create_gui(app, mixer, sound_file):
    #All this code is part of the function , so it needs to be indented.
    #This function is LOCAL to the "create_gui()" function.
    #A function-in-a function is called a local function.
    def track_toggle():
        if track_playing.get() == 1:
            track.play(loops = -1)
        else:
            track.stop()
    #This function is LOCAL, too.
    def change_volume(v):
        track.set_volume(volume.get())
#When this function is called, it starts excuting from here.
    track = mixer.Sound(sound_file)
    track_playing = IntVar()
    track_button = Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file)
#As always , the calls to  "pack()" add the widgets to the GUI.
    track_button.pack(side = LEFT)
    volume = DoubleVar()
    volume.set(track.get_volume())
    volume_scale = Scale(variable = volume, from_ = 0.0, to = 1.0, resolution = 0.1, command = change_volume, label = "Volume", orient = HORIZONTAL)
    volume_scale.pack(side = RIGHT)
