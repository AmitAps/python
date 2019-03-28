vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
#Create an empty dictionary.
found= {}


for letter in word:
    if letter in vowels:
        #Increment the value referred to by "found[letter]" by one.
        found[letter] += 1
#As the "for" loop is using the "items" method, we need to provide two loop variables, "k" for the key and "v" for the value.
                        #Invoke the "items" method on the "found" dictionary to access each row of data with each iteration.
for k, v in sorted(found.items()):
    #The key and the value are used to create each output message.
    print(k, 'was found', v, 'time(s).')
