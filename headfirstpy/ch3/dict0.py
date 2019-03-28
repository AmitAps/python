#Import the "pprint" module, then invoke the "pprint" function to do the work.
import pprint

person3 = { 'Name': 'Amit Pratap singh',
            'Gender': 'Male',
            'Occuption': 'Researcher',
            'Home Planet': 'India' }
#Start with a new empty dictionary.
#The key is "Ford" and the value is another dictionary.
people = {}
#The "people" dictionary contains another dictionary (which is the value associated with the "Amit" key.)
people['Amit'] = { 'Name': 'Amit Pratap singh',
            'Gender': 'Male',
            'Occuption': 'Researcher',
            'Home Planet': 'India' }

people['Arthur'] = { 'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupation': 'Sandwich-Maker',
                    'Home Planet': 'Earth' }

people['Trillian'] = { 'Name': 'Tricia McMillan',
		               'Gender': 'Female',
                       'Occupation': 'Mathematician',
                       'Home Planet': 'Earth' }
pprint.pprint(people)


#Accessing a complex Data Structure's Data
print(people['Arthur'])
print(people['Arthur']['Occupation'])
