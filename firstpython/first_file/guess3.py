from random import randint
secret = randint(1, 10)
#set guess to ZERO or some sensible value to make sure the loop run first time
guess = 0
print("Welcome to the gussing game")
while guess != secret:
    g = input("Guess a number betwween 1 to 6 ")
    guess = int(g)
    if guess == secret:
        print("Congrats you won!!!")
    else:
        if guess < secret:
            print("Too Low!")
        else:
            print("Too High!")
print("Game over. Thank you")
