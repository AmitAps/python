import urllib.request
import time
name_of = 'Amit'

while len(name_of) > 3:
    time.sleep(6)
    page = urllib.request.urlopen("https://www.flyhiee.com/")

    text = page.read().decode("utf8")
    where = text.find("Amit") #search for the index location of "Amit" combinationself.

    start_text = where + 0
    end_text = start_text + 17
    name = text[start_text:end_text]
#With the start and end index locations known, it’s easy to specify the substring required.
    print(name.capitalize())
print("Sorry, Not found!")
