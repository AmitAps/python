highest_score = 0
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split() #Add in the call to the split() method to cut the line in two, creating the "name" and "score" variables.
    if float(score) > highest_score: #you are no longer comparing the line to the highest score, so be sure to compare the "score" variable insted.

        #The "highest_score" variable gets updated every time you find a line that contains a higher score.

        highest_score = float(score) #you are no longer comparing the line to the highest score, so be sure to compare the "score" variable insted.
        # Remember to convert the string to a number with float(). Even though the line is a number, it comes into the program as a string.
result_f.close()
print("The highest score was:")
print(highest_score)
#After the loop runs, the "highest_score" variable  should have the best score from the data file, so you can then go ahead and display it on screen.
#Python strings have a built-in split() method. And you'll find that other programming languages have very similar mechanisms for breaking up strings.
