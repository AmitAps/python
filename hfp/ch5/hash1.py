scores = {} #You need to start with an empty hash as opposed to an empty array.
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores[score] = name #After splitting out the name and the score, and hash the of key the as the value of “score" the value of “name" as the value.
result_f.close()
print("The top scores were:")
for each_score in scores.keys(): #use for loop to process the contents of the hash.
    print('surer ' + scores[each_score] + 'scored ' + each_score) #Display each row from the hash, describing the association.
