#The interpreter creates two objects: one set and one string.
vowels = set('aeiou')

word = 'hello'

#Python converts the value in "word" into a set of letter objects (removing any duplicates as it does so).
#The "union" method combines one set with another,which is then assigned to a new variable called "u" (which is another set).
fuckyou = vowels.union(set(word))

#The "fuckyou" set consists of all the unique objects from both sets.

fuckoff = sorted(list(fuckyou))
#A sorted list of unique letters
print(fuckoff)


#Difference tells you what's not shared
#The "fuck_d" set consists of all the objects in "vowels" that aren't in "set(word)".
fuck_d = vowels.difference(set(word))
print(fuck_d)

#The difference function compares the objects in vowels against the
#objects in set(word), then returns a new set of objects (called d here)
#which are in the vowels set but not in set(word).

#Intersection Reports on Commonality
#The third set method that we’ll look at is intersection, which takes the objects in one set and compares them to those in another, then reports on any common objects found.
i = vowels.intersection(set(word))

print(i)
