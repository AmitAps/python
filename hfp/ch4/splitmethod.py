#The split() method cuts the string

rock_band = "Al Carl Mike Brian"
#Using a programming feature called multiple assignment, you can take the result from the cut performed by split() and assign it to a collection of variables.
(rhythm, lead, vocals, bass) = rock_band.split()
print(rock_band)
#The left side of the assignment operator lists the variables to assign values to
#The right side of the assignment contains the call to the split() method.
