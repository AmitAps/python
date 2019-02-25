input_word = input("Enter some words: ")
input_letter = input("Enter some letters: ")

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            print(word)
            return index
        index = index + 1
    print('Sorry No match Found! Try searching with other word')
    return -1

print(find(input_word, input_letter))
