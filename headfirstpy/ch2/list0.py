#A list is an ordered collection of objects

#How to spot a list in code?
#Lists are always enclosed in square brackets, and the objects contained within the list are alaways separated by a comma.

#Lists can be created literally or "grown" in code.

#Creating lists literally

#The variable name is on the left of the assignment operator and the "literal list" is on the right In this case, the list is empty.

prices = [] #This is an empty list.

#Objects (in this case, some floats) are separated by commas and surrounded by square brackets--it's a list.
temps =[ 32.0, 212.0, 0.0, 81.6, 100.0, 45.3]
#A list of string objects.
words = ['hello', 'world']

#A list of objects of different type.
car_details = ['Toyota', 'RAV4', 2.2, 60807]


#List inside of a list
everything = [prices, temps, words, car_details]

odds_and_ends = [[1, 2, 3], ['a', 'b', 'c'],['One', 'Two', 'Three']]

print(everything)
print(odds_and_ends)
