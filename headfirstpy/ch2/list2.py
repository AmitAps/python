#An empty list which the interpreter (thanks to "len") confirms has no objects.
found = []
#The "len" built-in function reports on the size of an object.
print(len(found))
for i in range(5):
    text_add = input("input a letter: ")
    #Add to an existing list at runtime using the "append" method.
    found.append(text_add)
    #Asking the shell to display the content of the list confirms the object is now part of the list.
    print(found)
#The length of the list has now incresed.
print(len(found))
