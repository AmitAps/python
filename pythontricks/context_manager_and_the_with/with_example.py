with open('hello.txt', 'w+') as f:
    f.write('Hello, World!')

    for line in f:
        print(line, end='')
