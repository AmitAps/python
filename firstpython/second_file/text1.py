import urllib.request

page = urllib.request.urlopen("https://www.flyhiee.com")
text = page.read().decode("utf8")
new_text = text[250:288]
#Index text[250:288] of the first charcter and the last character but last is not included
print(new_text)
