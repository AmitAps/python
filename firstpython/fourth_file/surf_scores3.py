scores = []
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
result_f.close()
print("The Top scores is")
print(scores[0])
print(scores[1])
print(scores[2])
