#A default value has been assigned to the "letters" argument and ill be used whenever the calling code doesn't provide an alternate value.
def search4letters(phrase:str, letters:str='aeiou') -> set:

    return set(letters).intersection(set(phrase))

print(search4letters('life, the univese, and everything'))
