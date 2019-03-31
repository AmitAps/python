def search4vowels(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase:str, letters:str='aeiou') -> set:
    return sorted(set(letters).intersection(set(phrase)))


#Share your functions in modules.
