#s[12] --> If you provide a single index after the variable name, you get a single characterself.
#s[138:147]-->  This will read the smaller substring from the entire string contained within "s".
#If you provide two index values, you extract a group of characters from the first index up to (But not including) the second indexself.
#In general, if you specify a substring using s[a:b], then a is the index of the first character  b is the index after the last character(Up to, but not including)

import urllib.request

page = urllib.request.urlopen("https://www.flyhiee.com/")

text = page.read().decode("utf8")

name = text[135:168]
print(name.upper())
