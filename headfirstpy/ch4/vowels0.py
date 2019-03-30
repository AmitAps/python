#Give your function a nice, descriptive name.
#Start with the "def" keyword.
                 #Provide an optional list of arguments-in this case, this function has no arguments, so the list is empty.
def search4vowels(): #Don't forget the colon.
    #A docstring has been added to the function's code, which (briefly) descrives the purpose of this function.
    #Be consistant in your use of string quote charachters.If possible, use single quotes.
    """Display any vowels found in an asked-for word."""
    #The five lines of code , suitably indented.
    vowels = set('aeiou')
    word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels()

#Be consistant in your use of string quote characters. If possible, use single quotes.
