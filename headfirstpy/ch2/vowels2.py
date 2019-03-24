vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Provide a word to search for vowels: ")

found = []
for letter in word:
    #This code displays the vowels in "word" as they are found.
    if letter in vowels:
        if letter not in found:
            #Include the code that decides whether to update the list of found vowels.
            found.append(letter)
#When the first "for" loop terminates, this second one gets to run, and it displays the vowels found in "word".
for vowel in found:
    print(vowel)
