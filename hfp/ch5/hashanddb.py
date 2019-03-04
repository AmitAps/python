def find_details(id2find):
    surfers_f = open("surfing_data.csv") #Open the file so that you can read the data.
    for each_line in surfers_f: #Use "for" to loop through each of the lines in the file.
        s = {} #Make sure to hash start empty
        (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = each_line.split(";")
                                                                                            #Cut up the line(using split()) and assign the data to the hash (using multiple-assignment).
        if id2find == int(s['id']): #Check if the ID supplied as a parameter in the same as the one read from the file.
            surfers_f.close
            #You have a match! So, close the file then return the current hash to the caller.
            return(s)
    surfers_f.close()
    return({})
    #You processed the entire file but found NO MATCH. Close the file and return an empty hash.

lookup_id = int(input("Enter the id of the surfer: "))
surfer = find_details(lookup_id)
if surfer:
    print("ID:          " + surfer['id'])
    print("Name:        " + surfer['name'])
    print("Country:     " + surfer['country'])  #Display six nicely formatted messages on screen.
    print("Average:     " + surfer['average'])
    print("Board type:  " + surfer['board'])
    print("Age:         " + surfer['age'])
else:
    print("Sorry! No match found")
