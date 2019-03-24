#Create a new list (and assign five number objects to it).
first = [1, 2, 3, 4, 5]
#The "first" list's five numbers
print(first)
#"Copy" the existing list to a new one, called "second".
second = first
#The "second" list's five numbers
print(second)

second.append(6)
#This seems okay, but isn't.
print(second)

#Whoops! The new object is appended to "first" too.
print(first)

#TO solve this problem, lists come with a copy method, which does the right thing.
third = second.copy()
print(third)

#The "third" list has grown by one object.
third.append(7)
print(third)
#Much better. The exxisting list is unchanged.
print(second)


#Don't use the assignment operatpr to copy a list; use the "copy" methid instead.
