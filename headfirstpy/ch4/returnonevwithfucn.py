#Returning one Value
def search4vowels(word):
    """Return a boolean based on any vowels found."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    #Call the "bool" functions, and pass in the name of the data structure that contains the results of the vowels search.
    return bool(found)

#The "return" statement (thanks to "bool") gives us either "True" or "False".
print(search4vowels('sky'))
