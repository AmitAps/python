#Use the "list" BIF to define an empty list, then assign some data.
l = list()
print(l)
l = [1, 2, 3]
print(l)

#Use the "dict" BIF to define an empty dictionary, then assign some data.
d = dict()
print(d)
d = { 'first': 1, 'second': 2, 'thirf': 3}
print(d)

#Use the "set" BIF to define an empty set, then assign some data.
s = set()
print(s)
s = {1, 2, 3}
print(s)

#Use the "tuple" BIF to define an empty tuple, then assign some data.
t = tuple()
print(t)
t = (1, 2, 3)
print(t)


#Even though sets are enclosed in curly braces, so too are dictionaries. An empty dictionary is already using the double curly braces, so an empty set has to be represented as “set()”.
