#Open a file hich has this filename and open the file in "append-mode".
todos = open('todos.txt', 'a')

#We print a message to the file stream.
print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)
#We're done. so let's tidy up after ourselves by closing the file stream.
todos.close()

#Open the file.
#Assign the file stream to a variable.
with open('todos.txt') as tasks:
    #Perform some processing(Which is the same code as before).
    for chore in tasks:
        print(chore, end='')


#Python supports "open, process, close." But most Python programmers prefer to use the "with" statement.