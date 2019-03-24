#insert: takes an index value and an object as its arguments
#The insert method inserts an object into an existing list before a specified index value.
#This lets you insert the object at the start of an existing list or anywherewithin the list. It is not possible to insert at the end of the list, as that’s what the append method does:
nums = [2, 3, 4]

            #The index of the object to insert *before*
nums.insert(0, 1)
               #The value to insert.

#The first argument to "insert" indicates the index value to insert *before*.
nums.insert(2, "two-and-a-half")
print(nums)
