                                   #The string -formatting operator.
print("There are %5d %s available." % (17, "donuts"))
                                    #OK, this string is followed by a % symbol. So... I ll need to replace %5d with the number 17, and %s with the string “donuts”.
                 #The first value will be inserted as a 5-character number.The second value will be inserted as a string.


#When Python sees a string followed by a percentage (%) symbol, it knows that it needs to consider the string as a string format. The values that follow the % operator are going to be inserted into
#the formatted string in the order specified, one value at a time. Wherever Python finds a % inside the string, it knows to insert a value.
