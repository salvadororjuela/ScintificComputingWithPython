"""To get credit for this assignment, perform the instructions below and upload your 
SQLite3 database here:
XXXXXXXXXXXXX Ningún archivo seleccionado
(Must have a .sqlite suffix)
Hint: The top organizational count is 536.
You do not need to export or convert the database - simply upload the .sqlite file 
that your program creates. See the example code for the use of the connect() statement.

Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of email 
messages per organization (i.e. domain name of the email address) using a database with 
the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for 
grading.
If you run the program multiple times in testing or with dfferent files, make sure to 
empty out the data before each run.

You can use this code as a starting point for your application: 
http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: 
http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the 
database as each record is read in the loop, it might take as long as a few minutes to 
process all the data. The commit insists on completely writing all the data to disk 
every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. 
In any database program, there is a balance between the number of operations you execute 
between commits and the importance of not losing the results of operations that have not 
yet been committed."""

import sqlite3

# Create database

conn = sqlite3.connect("organizationsDb.sqlite")
# cursor to send commands
cur = conn.cursor()
# If the table exists, drop it
cur.execute("DROP TABLE IF EXISTS Counts")
# Create the table to store data
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

# Get the file name
fname = input("Enter file name: ")
# Use the input file. If no input, use default
if (len(fname) < 1 ): fname = "mbox.txt"
# open file
fh = open(fname)

for data in fh:
    # Get only the lines that start with "From"
    if not data.startswith("From: "): continue
    # Split the line into words
    words = data.split()
    # Get the second word that correspond to the email.
    email = words[1]
    # Get the email url with the information after the @ symbol
    indexorg = email.split("@")
    organization = indexorg[1]
    # Verify if columns and rows are addecuate
    cur.execute("SELECT count FROM Counts WHERE org = ?", (organization, ))
    # Get each line of data and insert it into the table Counts
    row = cur.fetchone()
    # If the email appears for the first time
    if row == None:
        # Insert the row and set the count to 1
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (organization, ))
    # Else, if the email is already in the table, update the count and increase it by 1 of that specific email
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (organization, ))

# Commit the changes on each iteration
conn.commit()

# Variable with the statement to execute on each of the following iterations
sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    
cur.close