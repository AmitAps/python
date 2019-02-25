word1_input = input("Enter a word: ")
word2_input = input("Enter a word again: ")

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both(word1_input, word2_input)
