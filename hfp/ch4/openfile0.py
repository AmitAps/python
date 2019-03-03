#If you need to read from a file using Python, one way is to use the built-in open() command.
result_f = open("results.txt") #The open file assigned to a file handle, called "result_f" here.
#The call to open() creates a file handle, which is a shorthand that you’ll use to refer to the file you are working with within your code.

#Each time the body of the for loop runs, a variable is set to a string containing the current line of text in the file. This is referred to as iterating through the data in the file:
for each_line in result_f:
    #The "each_line" variable is set to the next line from the file on each iteration. The for loop stops when you run out of lines to read.
    print(each_line) #Do soemthing with the thing you've just read from the file. In this case, you print out the line. Notice that the for loop's code is indented.
result_f.close() #Close the file (through the file handle) when you're done with it.
