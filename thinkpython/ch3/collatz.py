n = 1027371

while n != 1:
    print(n, end=",  ")
    if n % 2 == 0: #n is even
        n = n // 2
    else: #n is odd
        n = n * 3 + 1
print(n, end=".\n")
