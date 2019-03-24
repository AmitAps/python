#pop: takes an optional index value as its argument
#The pop method removes and returns an object from an existing list based on the object's index value.
#If you invoke pop without specifying an index value, the last object in the list is removed and returned.
#If you specify an index value, the object in that location is removed and returned. If a list is empty or you invoke pop with a nonexistent index value, the interpreter raises an error
nums = [1, 2, 3, 4]
print(nums)

#You didn't tell "pop" which item to remove, so it operates on the last item in the list.
nums.pop()
print(nums)
#This is an index value. Zero corresponds to the first object in the list(the number 1)
nums.pop(0)
print(nums)
