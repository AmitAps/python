#The START value lets you control WHERE the range begins.
#When used with lists, the start value indicates the starting index value.

#The STOP value lets you control WHEN the range ends.
#When used with lists, the stop value indicates the index value to stop at , but not include.

#The STEP value lets you control HOW the range generated.
#When used with lists, the step value refers to the stride to take.


#You can put start, stop, and step inside square brackets.
#When used with lists, start, stop, and step are specified within the square brackets and are separated from one another by the colon (:) character:

#The square bracket notation is extended to work with start, stop, and step.
#letters[start:stop:step]

#When start is missing, it has a default value of 0.
#When stop is missing, it takes on the maximum value allowable for the list.
#When step is missing, it has a default value of 1.

saying = "Don't panic!"
letters = list(saying)

print(letters)

#List slices in Action
#This will print every third letter up to (but not including) index location 10.
print(letters[0:10:3])

#Skip the first three letters, then give me everything else.
print(letters[3:])

#All letters up to (but not including) index location 10.
print(letters[:10])

#Every second letter.
print(letters[::2])
