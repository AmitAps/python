line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"

s = {} #Create a empty hash called "s"
                                                                            #Cut the line of data every time the split() method sees a semicolon.
(s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = line.split(";")
#Use multiple- assignment to assign the split data from "line" to "s".
print("ID:          " + s['id'])
print("Name:        " + s['name'])
print("Country:     " + s['country'])  #Display six nicely formatted messages on screen.
print("Average:     " + s['average'])
print("Board type:  " + s['board'])
print("Age:         " + s['age'])
