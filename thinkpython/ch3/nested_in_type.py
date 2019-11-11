x = int(input("Enter the number between 0 to 10: "))
if 0 < x: #Assume x is an int here
    if x < 10:
        print("x is a positive single digit.")
#Only in single if statement

if 0 < x and x < 10:
    print("x is a positive single digit.")

if 0 < x < 10:
    print("x is a positive single digit.")
