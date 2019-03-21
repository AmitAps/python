print(range(5))
#Feeding the output from "range" to "list"  produces a list.
print(list(range(5)))

#We can adjust the START and STOP values for "range".
print(range(5, 10))
#It is possible to adjust the STEP value.
print(range(0, 10, 2))

#Things get really interesting when you adjust the range's direction by negating the STEP value.
print(list(range(10, 0, -2)))

#Python won't stop you from being silly. If your START value is bigger than STOP value, and STEP is positive, you get back nothing(in this case, an empty list).
print(list(range(10, 0, 2)))

print(list(range(99, 0, -1)))
