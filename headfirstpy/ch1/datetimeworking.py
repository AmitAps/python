import datetime
import time
#This will print today date.
print(datetime.date.today())

#You can access the day, month, and year values separately by appending an attribute access onto the call to date.today:
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

#You can also invoke the date.isoformat function and pass in today’s date to display a much more user-friendly version of today’s date, which is converted to a string by isoformat:
print(datetime.date.isoformat(datetime.date.today())) #Today's date as a string.

print(time.strftime("%H:%M:%S"))

print(time.strftime("%A %p"))
