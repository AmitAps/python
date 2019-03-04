#Data Structure A standard method of organizing a collection of data items in your computer's memory. You've already met one of the classic data structures: the array.
#Hashes go by different names in different programming languages: mapping, dictionary, associative array, and key-value list, to name a few.
#Associate a key with a value using a hash
scores = {} #Note the use of curly brackets here

#An empty hash is assigned to a variable called “scores"
#You add data to an existing hash by describing the association between the key and the value. Here’s how to associate a surfers’ name with their score:
scores[8.45] = 'Joseph' #A new row of data is added to  the hash.
#put the key inside the square brackets and put the value to the right of the assignment operator.

#Note how the act of assigning a value to a key CREATES the hash entry (assuming it's not already there). In Python, there's no
#explicit “append()" method for hashes as there is for arrays.
scores[9.12] = 'Juan'
scores[7.21] = 'Zack'

#Once you have a hash created, you can use the trusty for loop to iterate over each of the rows:
                  #The "keys()" built-in method returns an array of the keys of the hash. There are no extra points for guessing what the "values()" method does.
for key in scores.keys(): #Take each of the keys in the hash in turn ...and display a custom message using the data in each row of the hash.
    print(scores[key] + ' had a score of ' + str(name_part))
                #when referring to a value associated with a key, use square brackets(Just like array).



#Another hash method, called items(), returns each key-value pair in turn, and can be used with the for loop, too:
for score, surfer in scores.items(): #The “items()” method returns each key-value pair.

    print(surfer + ' had a score of ' + str(score))
