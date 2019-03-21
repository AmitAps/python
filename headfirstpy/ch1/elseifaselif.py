#elseif is replaced by elif in Python.

#Three individual suites: one for the "if", another for the "elif" and the final catch-all for the "else".
today = input("Enter the day: ")
condition = input("Enter the condition of your body: ")
if today == 'Saturday':
    print('Party!!')
elif today == 'Sunday':
    if condition == 'Headache':
        print('Recover , then rest.')
    else:
        print('Rest.')
else:
    print('Work, work, work.')

#Indentation is important in Python program .

#The if, elif, and else keywords precede blocks of code, which are known in the Python world as “suites.”
#It is easy to spot suites of code, as they are always indented. Indentation is the only code grouping mechanism provided by Python.
#In addition to indentation, suites of code are also preceded by a colon ( : ). This is a syntactical requirement of the language.
