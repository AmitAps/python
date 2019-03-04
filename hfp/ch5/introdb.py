#Import the standard SQLite3 library and connect to the data in the database file.
import sqlite3
db = sqlite3.connect("surfersDB.sdb")
#Grab all the surfer data from the database, assigining the data to a variable called "rows".
db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute("select * from surfers")
rows = cursor.fetchall()
for row in rows: #Process each of the rows
    if row['id'] == 104: #looking for a surfer who has an id of 104.
        #print out some of the data(If we have a match).
        print("ID is " + str(row['id']))
        print("Name is " + row['name'])
        print("Board-type is " + row['board'])
cursor.close()
