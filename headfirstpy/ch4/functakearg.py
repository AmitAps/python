#Functions can Accept Arguments
#Put the argument's name between the parentheses.
def search4vowels(word):
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    #This line isn't needed anymore.
    #word = input('Provide a word to search for vowels: ')
#The call to the "input" function is gone(as we don't need that line of code anymore).

    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels('amitpratapsingh')
