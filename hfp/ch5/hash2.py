scores = {} #You need to start with an empty hash as opposed to an empty array.
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores[score] = name #After splitting out the name and the score, and hash the of key the as the value of “score" the value of “name" as the value.
result_f.close()
print("The top scores were:")
                                        #Remember: the keys in your hash are the scores, which are numbers, so we ask "sorted()" to order them highest-to-lowest using "reverse = True".
for each_score in sorted(scores.keys(), reverse = True): #use for loop to process the contents of the hash.
                  #Use the "sorted()" function to sort the keys of the "scores" hash.
    print('surer ' + scores[each_score] + ' scored ' + each_score) #Display each row from the hash, describing the association.

#Now that you are sorting the keys of the hash (which represent the surfer’s scores), it should be clear why the scores were used as the key when adding
#data into the hash: you need to sort the scores, not the surfer names, so the scores need to be on the left side of the hash (because that’s what the built-in sorted() function works with).
