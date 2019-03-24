#extend: takes a list of objects as its sole argument
#The extend method takes a second list and adds each of its objects to an existing list. This method is very useful for combining two lists into one:
nums = [2]

#Provide a list of objects to append to the existing list.
nums.extend([3, 4])

#Using an empty list here is valid, if a little silly (as you're adding no items to the end of an existing list). If you'd instead called "append([])", an empty list would be added to the end of the existing list, but-in this example-using "extend([])" does nothing.

nums.extend([])
print(nums)
