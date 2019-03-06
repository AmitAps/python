#You need to import pygame's "mixer" module in order to play sounds.

import pygame.mixer
#Reuse the "wait_finish()" function from earlier.
def wait_finish(channel):
    while channel.get_busy():
        pass
#Create a mixer object and initialize the pygame sound system.
sounds = pygame.mixer

sounds.init()

#Load each of the required sounds into its own variable.
correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

#This is what you'll ask the question master each time.
prompt = "Press 1 for Correct, 2 for Wrong, or 0 to Quit: "

#Make sure the counts that you'll maintain are set to a resonable starting value.
#It would be ok to move these three lines of code to the top of the program, just so long as they have starting values before the while loop starts.
number_asked = 0
number_correct = 0
number_wrong = 0

#Prompt the host
choice = input(prompt)
#while the game hasn't ended..
while choice != '0':
    #If the answer is correct, increment the counters and then play the appropriate sound..
    if choice == "1":
        number_asked = number_asked + 1
        number_correct = number_correct + 1
        wait_finish(correct_s.play())
        #If the answer is incorrect, increment the cpinters and play the sound effect.
    if choice == "2":
        number_asked = number_asked + 1
        number_wrong = number_wrong + 1
        wait_finish(wrong_s.play())
    choice = input(prompt)
#At the end of the program display a summary of the counter values.
print("You asked " + str(number_asked) + " questions.")
print(str(number_correct) + " were correctly answered.")
print(str(number_wrong) + " were answered incorrectly.")
