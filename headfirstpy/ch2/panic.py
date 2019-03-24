#We are starting with a string.
phrase = "Don't panic!"
#We turn the string into a list.
plist = list(phrase)
#We display the string and the list on screen.
print(phrase)
print(plist)
#This small loop pops the last four objects from "plist".
for i in range(4):
    plist.pop()
#Get rid of the "D" at the start of the list.
plist.pop(0)
#Find , then remove , the apostrophe from the list.
plist.remove("'")

#Swap the two objects at the end of the list by first popping each object from the list , then using the popped the list.
#This is a line of code that you'll need to think about for a little bit key point the pops occur *first* (in the order shown), then the extend happens.
plist.extend([plist.pop(), plist.pop()])
#This line of code pops the space from the list, then inserts it back into the list at index location 2. Just like the last line of code, the pop occurs *first*, before the insert happens. And, remember: spaces are charachters, too.
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
