Python 3.7.5 (default, Oct 17 2019, 12:16:48) 
[GCC 9.2.1 20190827 (Red Hat 9.2.1-1)] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/writing_complete_program/guess_number.py
Hello. What is your name?
Amit
Well, Amit, I am thinking of a number between 1 and 20.
Take a guess.
15
Your guess is too high.
Take a guess.
10
Your guess is too low.
Take a guess.
13
Your guess is too high.
Take a guess.
12
Your guess is too high.
Take a guess.
11
Traceback (most recent call last):
  File "/home/Aps/workspace/python/Automate_with_python/writing_complete_program/guess_number.py", line 23, in <module>
    print('Good job, ' + name + '! you gusses my number in ' + str(guesssesTaken) + ' guesses!')
NameError: name 'guesssesTaken' is not defined
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/writing_complete_program/guess_number.py
Hello. What is your name?
Amit pratap singh
Well, Amit pratap singh, I am thinking of a number between 1 and 20.
Take a guess.
13
Your guess is too high.
Take a guess.
9
Your guess is too high.
Take a guess.
5
Your guess is too high.
Take a guess.
2
Good job, Amit pratap singh! you gusses my number in 4 guesses!
You took 4 guesses.
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/writing_complete_program/guess_number.py
Hello. What is your name?
aps
Well, aps, I am thinking of a number between 1 and 20.
Take a guess.
1
Your guess is too low.
Take a guess.
1
Your guess is too low.
Take a guess.
1
Your guess is too low.
Take a guess.
1
Your guess is too low.
Take a guess.
1
Your guess is too low.
Take a guess.
1
Your guess is too low.
Nope, The number i was thinking of was 11
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/writing_complete_program/guess_number.py
Hello. What is your name?
aps
Well, aps, I am thinking of a number between 1 and 20.
DEBUG: Secret number is 12
Take a guess.
12
Good job, aps! you gusses my number in 1 guesses!
>>> 
= RESTART: /home/Aps/workspace/python/Automate_with_python/writing_complete_program/guess_number.py
Hello. What is your name?
aps
Well, aps, I am thinking of a number between 1 and 20.
DEBUG: Secret number is 14
Take a guess.
13
Your guess is too low.
Take a guess.
15
Your guess is too high.
Take a guess.
