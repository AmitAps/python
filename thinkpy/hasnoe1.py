fin = open('words.txt')

def has_no_e(fin):
    for word in fin:
        line = word.strip()
        if 'e' != line:
            print(line)
        
            
        
print(has_no_e(fin))
