line1 = input("Enter a line: ")
line2 = input("Enter another line: ")

def cat_twice(part1, part2): #This function takes two arguments, concatenates them, and prints the result twice.
    cat = part1 + part2 #When you create a variable inside a function, it is local, which means that it only exists inside the function.
    print(cat)

cat_twice(line1, line2)


#When cat_twice terminates, the variable cat is destroyed. If we try to print it, we get an exception:
# >>> print(cat)
# NameError: name 'cat' is not defined
