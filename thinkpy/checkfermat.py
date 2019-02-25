a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
n = int(input("Enter a number: "))

def check_fermat(a, b, c, n):
    if ((a ** n) + (b ** n)) == ( c ** n):
        print("WTF, Fermat was wrong")
    else:
        print("Fermat was right")

check_fermat(a, b, c, n)
