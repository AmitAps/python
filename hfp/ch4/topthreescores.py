scores = []
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
result_f.close() #At this point in the code, the array is in memory but it's not in the order you need. It's unsorted.
scores.sort()
#The sort() and reverse() methods look the most useful. You need to use reverse() after you sort() the data, because the default ordering used by sort() is lowest-to-highest, the opposite of what you need.
scores.reverse()
print("The top three score were:")
for i in range(3):
    print(scores[i])
#print(scores[0])
#print(scores[1])
#print(scores[2])

#It was very simple to sort an array of data using just two lines of code. But it turns out you can do even
#better than that if you use an option with the sort() method. Instead of using these two lines:
		 #scores.sort()
		 #scores.reverse()
#you could have used just one, which gives the same result: scores.sort(reverse = True)
