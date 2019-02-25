n = int(input("Enter an integer: "))

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        print('Blastoff!')

countdown(n)
