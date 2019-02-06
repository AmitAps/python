import urllib.request
page = urllib.request.urlopen("https://www.flyhiee.com")
text = page.read().decode("utf8")

where = text.find("Amit")

start_of_string = where
end_of_string = start_of_string + 17

full_string = text[start_of_string:end_of_string]

print(full_string)
