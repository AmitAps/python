#Import the required libraries
from tkinter import *
import pygame.mixer

from tkinter.messagebox import askokcancel

#Create the GUI application window.
app = Tk()
app.title("Head first mix")

#Identify the DJ's track
sound_file = "50459_M_RED_Nephlimizer.wav"

#Start the sound system.
mixer = pygame.mixer
mixer.init()

#The "track_toggle" function either plays or stops the track, based on the state of the checkbox.
def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    else:
        track.stop()

def change_volume(v):
    track.set_volume(volume.get())

#Load up the track sound file.
track = mixer.Sound(sound_file)
track_playing = IntVar()
                                                                                  #Use the name of the sound file as the text associated with the checkbox.
track_button = Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file)

track_button.pack(side = LEFT)
volume = DoubleVar()
volume.set(track.get_volume())

volume_scale = Scale(app, variable = volume, from_ = 0.0, to = 1.0,  resolution = 0.1, command = change_volume, label = "Volume", orient = HORIZONTAL)
volume_scale.pack(side = RIGHT)
#Simply arrange for the track to stop playing when the window closes.
def shutdown():
    track.stop()
    if askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
        app.destroy()





#Call "app.protocol()" before the call to "app.mainloop()".
app.protocol("WM_DELETE_WINDOW", shutdown)

#Start the Gui event loop.
app.mainloop()


#No matter how often you click the close box, the window won't go away..
