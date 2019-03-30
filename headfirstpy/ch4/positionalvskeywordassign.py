def search4letters(phrase:str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase))
#The ordering of the arguments isn't important when keyword arguments are used during invocation.
print(search4letters(letters='xyz', phrase='galaxy'))
