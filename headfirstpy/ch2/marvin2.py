paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
    #On each iteration, this variable refers to the current object.
            #This is the list to iterate over.
#The first loop iterates over a slice of the first six obects in the list.
for char in letters[:6]:
    #This block of code excutes on each iteration.
    #Each character from the "letters" list is printed on its own line, preceded by a tab character(that's what the \t does).
    print('\t', char)
print()
#The second loop iterates over a slice of the last seven objects in the list. Note how "*2" inserts two tab characters before each printed object.
for char in letters[-7:]:
    print('\t'*2, char)
print()
#The third (and final) loop iterates over a slice from within the list selecting the characters that spell the word "Paranoid".Note how "*3" inserts three tab characters before each printed object.
for char in letters[12:20]:
    print('\t'*3, char)
