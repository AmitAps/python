n = int(input('Enter an integer: '))
s = input('Enter a string: ')

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
    
print_n(s, n)

#If n <= 0 the return statement exits the function. The flow of execution immediately returns to the caller, and the remaining lines of the function don’t run.
