
#Specify the list of arguments, and don't forget the colon (and the annotations, too).

def search4letters(phrase:str, letters:str) -> set:
    #Create a set object from "letters" .
    #Perform a set intersection on the set object made from "letters" with the set object made from "phrase".
    #Send the results back to the calling code.
    return set(letters).intersection(set(phrase))

print(search4letters('galaxy', 'xyz'))
