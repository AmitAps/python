n = int(input('Enter an integer: '))

def countdown(n):
    if n <= 0:
        print('something')
    else:
        print(n)
        countdown(n-1)

countdown(n)


#A function that calls itself is recursive; the process of executing it is called recursion.
