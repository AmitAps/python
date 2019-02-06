import urllib.request


password="APS_._113920"

def send_to_twitter(msg):
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API",
                   "http://twitter.com/statuses", "Flyhieeofficial", password)
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode( {'status': msg} )
    resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
    resp.read()

def get_name():
    page = urllib.request.urlopen("https://www.flyhiee.com")
    text = page.read().decode("utf8")
    where = text.find("Amit")

    start_of_string = where
    end_of_string = start_of_string + 17

    return (text[start_of_string:end_of_string])

print("Welcome to the Get Name function board")
ask = input("Do you want a name to be displayed:(Y/N) ")
if ask == "Y":
    send_to_twitter(get_name())
else:
    print("No! Thank you . Not interested!!")

#If you use the return() command within a function, you can send a data value back to the calling code.
