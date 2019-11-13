Python 3.7.5 (default, Oct 17 2019, 12:16:48) 
[GCC 9.2.1 20190827 (Red Hat 9.2.1-1)] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except_example.py
21.0
3.5
Traceback (most recent call last):
  File "/home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except_example.py", line 6, in <module>
    print(div42by(0))
  File "/home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except_example.py", line 2, in div42by
    return 42 / divideBy
ZeroDivisionError: division by zero
>>> 40 / 0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    40 / 0
ZeroDivisionError: division by zero
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except_example1.py
21.0
3.5
Error: You tried to divide by zero.
None
42.0
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except2.py
How many cats do you have?
2
That is not that many cats.
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except2.py
How many cats do you have?

Traceback (most recent call last):
  File "/home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except2.py", line 3, in <module>
    if int(numCats) >= 4:
ValueError: invalid literal for int() with base 10: ''
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except2.py
How many cats do you have?
six
Traceback (most recent call last):
  File "/home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except2.py", line 3, in <module>
    if int(numCats) >= 4:
ValueError: invalid literal for int() with base 10: 'six'
>>> int('6')
6
>>> int('six')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int('six')
ValueError: invalid literal for int() with base 10: 'six'
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except2.py
How many cats do you have?
six
You did not enter a number.
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/handling_error_with_tryexcept/try_except1.py
How many cats do you have?
3
That is not that many cats.
>>> 
