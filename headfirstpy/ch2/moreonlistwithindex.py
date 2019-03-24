#Python's lists understand positive index values, which start from 0 as well as negative index values, which start from -1.
saying = "Don't panic!"
#Create a list of letters.
letters = list(saying)
print(letters)
#Using positive index values counts from left to right..
print(letters[0])
print(letters[3])
print(letters[6])
#...Whereas negative index values count right to left.
print(letters[-1])
print(letters[-3])
print(letters[-6])

#It's easy to get at the first and last objects in any list.
first = letters[0]
last = letters[-1]

print(first, last)
