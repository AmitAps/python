import urllib.request
page = urllib.request.urlopen("#")
text = page.read().decode("utf8")

print(text)
