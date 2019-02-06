import urllib.request

def get_name():
    page = urllib.request.urlopen("https://www.flyhiee.com")
    text = page.read().decode("utf8")
    where = text.find("Amit")

    start_of_string = where
    end_of_string = start_of_string + 17

    print(text[start_of_string:end_of_string])
get_name()

#If you use the return() command within a function, you can send a data value back to the calling code.
