#In C++ and Java, a dictionary is known as "map", whereas Perl and Ruby use the name "hash".

#Data that conforms to the dictionary model is easy to spot: there are two columns, with potentially multiple rows of data.

#person: The name of the dictionary.
            #The key     #The associated data value
person = { 'Name': 'Ford Prefect',
            'Gender': 'Male',
            'Occuption': 'Researcher',
            'Home Planet': 'Betelgeuse Seven' }

#How to spot a dictionary in code

#An opening curly brace starts each dictionary.
#Each key is enclosed in quotes.
#In this dictionary, the values are all string objects, so they are enclosed in quotes.
#Each key/value pair is separated from the next by a comma.
#A colon associated each key with its value.
#A closing curly brace ends each dictionary.

print(person)
#Use key to access data in a dictionary.
#Provide the key between the square brackets.
print(person['Name'])

#Assign an object (in this case, a number) to a new key to add a row of data to the dictionary.
person['Age'] = 26

print(person)
