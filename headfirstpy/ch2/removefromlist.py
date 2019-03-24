#remove: takes an object's value an its sole argument

#The remove method removes the first occurrence of a specified data value from a list. If the data value is found in the list, the object that contains it is removed from the list (and
#the list shrinks in size by one). If the data value is not in the list, the interpreter will raise an error
nums = [1, 2, 3, 4]

print(nums)
                  #This is *not* an index value, it's the value to remove.
nums.remove(3)
#After the call to "remove", the object with 3 as its value is gone.
print(nums)
