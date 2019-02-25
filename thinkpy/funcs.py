def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
#def is a keyword that indicates that this is a function definition. The name of the
#function is print_lyrics . The rules for function names are the same as for variable
#names: letters, numbers and underscore are legal, but the first character can’t be a
#number. You can’t use a keyword as the name of a function, and you should avoid
#having a variable and a function with the same name.

#The empty parentheses after the name indicate that this function doesn’t take any arguments.
#The first line of the function definition is called the header; the rest is called the
#body. The header has to end with a colon and the body has to be indented. By con‐
#vention, indentation is always four spaces. The body can contain any number of statements.

#The syntax for calling the new function is the same as for built-in functions:
print_lyrics()
print("Above print is from the first function call")


#Once you have defined a function, you can use it inside another function. For example, to repeat the previous refrain, we could write a function called repeat_lyrics :
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

#And then call repeat_lyrics :
print("Below print is from the Last function call")   
repeat_lyrics()
