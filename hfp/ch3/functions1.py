import urllib.request
name_of = input("Enter your name: ")
def get_name(): #You need a colon after the function name.
    while len(name_of) > 3:
        page = urllib.request.urlopen("https://www.flyhiee.com/")

        text = page.read().decode("utf8")
        where = text.find("Amit") #search for the index location of "Amit" combinationself.

        start_text = where + 0
        end_text = start_text + 17
        name = text[start_text:end_text]
        print(name.capitalize()) #The function definition ends here.
#With the start and end index locations known, it’s easy to specify the substring required.
name_now = input("Do you want to see the name: ")
print("Welcome to the find and print name function from a webapage!")
get_name() #This line isn't indented because it is part of the main program.
print("Sorry, Name! Not found! Your name must be atlest 4 letter!")
