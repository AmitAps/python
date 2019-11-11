Python 3.7.3 (default, May 11 2019, 00:38:04) 
[GCC 9.1.1 20190503 (Red Hat 9.1.1-1)] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> phonebook = {
	'Amit': 9599404844,
	'Mukul': 9584755554,
	'Kshitij':6445512555,
	}
>>> squares = {x: x * x for x in range(6)}
>>> phonebook['Amit']
9599404844
>>> squares
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> 
>>> import collections
>>> d = collections.OrderdDict(one=1, two=2, three=3)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d = collections.OrderdDict(one=1, two=2, three=3)
  File "/usr/lib64/python3.7/collections/__init__.py", line 55, in __getattr__
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
AttributeError: module 'collections' has no attribute 'OrderdDict'
>>> d = collections.OrderedDict(one=1, two=2, three=3)
>>> d
OrderedDict([('one', 1), ('two', 2), ('three', 3)])
>>> d['four'] = 4
>>> d
OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
>>> d.keys()
odict_keys(['one', 'two', 'three', 'four'])
>>> 
>>> from collections import defaultdict
>>> dd = defaultdict(list)
>>> dd['dogs'].apped('Rufus')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dd['dogs'].apped('Rufus')
AttributeError: 'list' object has no attribute 'apped'
>>> dd['dogs'].append('Rufus')
>>> dd['dogs'].append('Kathrin')
>>> dd['dogs'].append('Mr Sniffles')
>>> dd['dogs']
['Rufus', 'Kathrin', 'Mr Sniffles']
>>> from collections import ChainMap
>>> dict1 = {'one': 1, 'two': 2}
>>> dict2 = {'three': 3, 'four': 4}
>>> chain = ChainMap(dict1, dict2)
>>> chain
ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})
>>> chain['three']
3
>>> chain['one']
1
>>> chain['missing']
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    chain['missing']
  File "/usr/lib64/python3.7/collections/__init__.py", line 914, in __getitem__
    return self.__missing__(key)            # support subclasses that define __missing__
  File "/usr/lib64/python3.7/collections/__init__.py", line 906, in __missing__
    raise KeyError(key)
KeyError: 'missing'
>>> 
>>> 
>>> #types.MappingProxyType – A Wrapper for Making Read-Only Dictionaries
>>> 
>>> from types import MappingProxyType
>>> writable = {'one': 1, 'two': 2}
>>> read_only = MappingProxyType(writable)
>>> #The proxy is read-only:
>>> read_only['one']
1
>>> read_only['one'] = 23
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    read_only['one'] = 23
TypeError: 'mappingproxy' object does not support item assignment
>>> #Updates to the original are refltected in the proxy:
>>> writable['one'] = 42
>>> read_only
mappingproxy({'one': 42, 'two': 2})
>>> d.values()
odict_values([1, 2, 3, 4])
>>> 
