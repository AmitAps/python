#A list of individual strings.
names = ['Amit', 'Disha', 'Mukul', 'Ankit', 'kshitij', 'Priya']
#The join trick in action.
pythons = '|'.join(names)

print(pythons)

#Take the string and split it into a list using the given delimiter.
individuals = pythons.split('|')
print(individuals)