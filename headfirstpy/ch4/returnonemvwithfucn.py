def search4vowels(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    #Return the results as a data structure(a set).
    return found

print(search4vowels('amit pratapsingh'))
