#Open a file hich has this filename and open the file in "append-mode".
todos = open('todos.txt', 'a')

#We print a message to the file stream.
print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)
#We're done. so let's tidy up after ourselves by closing the file stream.
todos.close()

#Reading data from an existing file.
#Open a file which has this filename.
tasks = open('todos.txt')
#Think of "chore" as an alias for the line in the file.
for chore in tasks: #The tasks variable is the file stream.
    print(chore, end='')

#We're done, so let's tidy up after ourselves by closing the file stream.
tasks.close()