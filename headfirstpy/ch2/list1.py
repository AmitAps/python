vowels = ['a', 'e', 'i', 'o', 'u']

word = "Milliways"

for letter in word: #Take each letter in the word...
    if letter in vowels: #... and if it is in the "vowels" list..
        print(letter) #...display the letter on screen.
