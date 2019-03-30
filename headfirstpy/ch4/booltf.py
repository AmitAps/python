#Something is False if it evaluates to 0, the value None, an empty string, or an empty built-in data structure.

#If an object evaluates to 0, it is always False.
print(bool(0))
print(bool(0.0))
#An empty string, an empty list, and an empty dictionary all evaluate to False.
print(bool(''))
print(bool([]))
print(bool({}))
#Python's "None" value is alays False.
print(bool(None))


#Every other object in Python evaluates to True.

#A number that isn't 0 is always True, even when it's negative.
print(bool(1))
print(bool(-1))
print(bool(42))

#It may be really small, but it is still not 0, so it's True.
print(bool(0.00000000000000000000000000000000000000000000000001))
#A nonempty string is always true.
print(bool('Panic'))
#A nonempty built-in data structure is True.
print(bool([42, 43, 44]))
print(bool({'a': 42, 'b':42}))
