import sqlite3

# Connection to the database, it is like a handle
conn = sqlite3.connect("emaildb.sqlite")
# Establish the cursor to send commands
cur = conn.cursor()
# If the table exists it drops it
cur.execute("DROP TABLE IF EXISTS Counts")
# If the table does not exists, create it
cur.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")

# Get the file name
fname = input("Enter file name: ")
# if no file name is provided, use the default one
if (len(fname) < 1): fname = "mbox-short.txt"
# open file
fh = open(fname)

for line in fh:
    # verify if the line starts with from
    if not line.startswith("From: "): continue
    # split the line into words
    pieces = line.split()
    # get the email word
    email = pieces[1]
    # The following line verifies that columns and rows are addecuate.
    cur.execute("SELECT count FROM Counts WHERE email = ?", (email,))
    # row is created to grab the information from the db.
    row = cur.fetchone()
    if row is None:
        # create a new row in the db if row has no information and set count to 1
        cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (email,))
    else:
        # if the row already exist, update the count adding 1
        cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (email,))
    # commit the changes on each iterations
    conn.commit()
    
# Variable with the statement to execute on each of the following iterations
sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"

# display the database info according to the previous sentence.
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the connection
cur.close()