word_input = input("Enter a word or sensence: ")
letter_input = input("Enter a letter: ")


def count_letter(word, letter):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

count_letter(word_input, letter_input)
    
