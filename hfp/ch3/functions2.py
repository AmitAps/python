import urllib.request

def get_name(): #You need a colon after the function name.
    page = urllib.request.urlopen("https://www.flyhiee.com/")
    text = page.read().decode("utf8")
    where = text.find("Amit") #search for the index location of "Amit" combinationself.
    start_text = where + 0
    end_text = start_text + 17
    name = text[start_text:end_text]
    return str((name.capitalize())) #The function definition ends here.
#With the start and end index locations known, it’s easy to specify the substring required.
name_now = input("Do you want to see the name: ")
if name_now == "Y":
    print(get_name())
else:
    name_of = input("Enter your name: ")
    while len(name_of) > 3:
        names = get_name()
        print(names)
    print("Please! Enter a name at least FOUR character long.")
