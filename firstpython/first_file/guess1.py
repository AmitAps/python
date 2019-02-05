print("Welcome to the gussing game")
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
