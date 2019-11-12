spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))



"""
When the excution reaches the end of a while statement's block, it jumps back to the start
to re-check the condition.

Press Ctrl-C to interrupt an infinite loop.

A break statement causes the excution to immediately leave the loop, without re-checking the condition.

A continue statement causes the excution to immediately jump back to the start of the loop
if_else.py
"""
