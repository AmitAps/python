f = open('hello1.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()
