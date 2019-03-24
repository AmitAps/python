book = "The Hitchhiker's Guide to the Galaxy"

booklist = list(book)
#Note that the original string contained a single quote character. Python is smart enough to spot this, and surrounds the single quote character with double quotes.
print(booklist)

#Select the first three objects (letters) from the list.
print(booklist[0:3])

#Turn the selected range into a string.
print(''.join(booklist[0:3]))

#This will Selects the last six objects from the list.
print(''.join(booklist[-6:]))

#This will print the original string reversed.
backwards = booklist[::-1]
print(''.join(backwards))

#"every_other" is a list made up from every second object(letter) starting from the first and going to the last Note: "start" and "stop" are defaulted.
every_other = booklist[::2]
print(''.join(every_other))

#A "slice" is a fragment of a list.
#Slice the word "Hitchhiker".
print(''.join(booklist[4:14]))
#Slice out the word "Hitchhiker", but do it in reverse order(i.e.,backward).
print(''.join(booklist[13:3:-1]))
