#Import the required libraries
from tkinter import *
import pygame.mixer

#Create the GUI application window.
app = Tk()
app.title("Head first mix")
app.geometry('250x100+200+100')

#Identify the DJ's track
sound_file = "50459_M_RED_Nephlimizer.wav"

#Start the sound system.
mixer = pygame.mixer
mixer.init()

#The "track_start()" function will respond to the "Start" button-click event.
#The "loops = -1" parameter to "play()" repeats the track until you stop it.
def track_start():
    track.play(loops = -1)

#The "track_stop()" function will respond to the "Stop" button-click event.
def track_stop():
    track.stop()

#Load up the track sound file.
track = mixer.Sound(sound_file)

#Create a button for "Start" and "Stop", then connect each of them to their event handlers.
start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)

stop_button = Button(app, command = track_stop, text = "stop")
stop_button.pack(side = RIGHT)

#Start the Gui event loop.
app.mainloop()
