print("Welcome to the gussing game")
#set guess to ZERO or some sensible value to make sure the loop run first time
guess = 0
while guess != 5:
    g = input("Guess a number betwween 1 to 6 ")
    guess = int(g)
    if guess == 5:
        print("Congrats you won!!!")
    else:
        if guess < 5:
            print("Too Low!")
        else:
            print("Too High!")
print("Game over. Thank you")
