print("Welcome")
guess = 0
while guess != 5:
    g = input("Guess the number: ")
    guess = int(g)
    if guess == 5:
        print("You win!")
    else:
        if guess > 5:
            print("Too High")
        else:
            print("Too Low")
print("Game over")
