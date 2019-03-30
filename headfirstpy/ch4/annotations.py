#Function annotations are optional
#Function annotations are informational
#We are stating that the "word" argument is expected to be a string.
#We are stating that the function returns a set to its caller.
def search4vowels(word:str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    #Return the data without the use of the unnecessary "found" variable.
    return vowels.intersection(set(word))
print(search4vowels('amit pratap singh'))
print(help(search4vowels))
