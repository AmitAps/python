#The "word variable is now called "phrase".
def search4vowels(phrase:str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(phrase))
    #Return the results as a data structure(a set).
    return found

print(search4vowels('amit pratapsingh'))

#Give the new function a more generic name.
#Add a second argument
#Remove the vowels variable
#Update the docstring
