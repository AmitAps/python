highest_score = 0
result_f = open("results.txt")
for line in result_f:
    if float(line) > highest_score:
        #The "highest_score" variable gets updated every time you find a line that contains a higher score.
        highest_score = float(line)
        # Remember to convert the string to a number with float(). Even though the line is a number, it comes into the program as a string.
result_f.close()
print("The highest score was:")
print(highest_score)
#After the loop runs, the "highest_score" variable  should have the best score from the data file, so you can then go ahead and display it on screen.
