fuel = int(input("Enter the fuel in tank: "))

if fuel > 3: #the first if branch
    print("It's ok!")
    print("You can drive downtown.")
else:
    money = int(input("Enter the Money: "))
    if money > 10: #This second if branch is connected to the "False" path of the first if branch.
        print("You should buy gas")
    else:
        print("You better stay at home")
        #notice the extra indentation.
print("What's next?")
