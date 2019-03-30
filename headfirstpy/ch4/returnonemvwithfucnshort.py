def search4vowels(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    #Return the data without the use of the unnecessary "found" variable.
    return vowels.intersection(set(word))

print(search4vowels('sky'))

#An empty set is represented as set() by the interpreter.

#You may have expected the function to return {} to represent an empty set, but that’s a common misunderstanding, as {} represents an empty dictionary,
 
