#Curly braces on their own mean the dictionary starts out empty.
found = {}

print(found)
#We've initialized all the vowel counts to 0.
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
print(found)

#Updatin a Frequency Counter
found['e'] = found['e'] + 1 #Increment e's count.
found['e'] += 1 #Increment e's count(once more)
print(found)

#Iterating over keys and values
#To access the associated data values, you need to put each key within square brackets and use it together with the dictionary name to gain access to the values associated with the key.

#we're using "k" to represent the key , and "found[k]" to access the value.
for k in found:
    print(k, 'was found', found[k], 'time(s).')

print()
print()
#Specifying the ordering of a dictionary on output
for k in sorted(found):
    print(k, 'was found', found[k], 'time(s).')


print()
print()
#The "items" method passes back two loop variables.
#We invoke the "items" method on the "found" dictionary.
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
