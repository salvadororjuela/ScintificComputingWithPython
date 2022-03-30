import json
import sqlite3

# Create the database
conn = sqlite3.connect('rosterdb.sqlite')
# Connection to the database. It is the file handler
cur = conn.cursor()

# Tables creation. Member has two foreign keys. This table is the joining table for the many to many relationship
cur.executescript("""
                  DROP TABLE IF EXISTS User;
                  DROP TABLE IF EXISTS Member;
                  DROP TABLE IF EXISTS Course;
                  
                  CREATE TABLE User (
                      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                      name TEXT UNIQUE
                  );
                  
                  CREATE TABLE Course (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    title TEXT UNIQUE  
                  );
                  
                  CREATE TABLE Member (
                      user_id INTEGER,
                      course_id INTEGER,
                      role INTEGER,
                      PRIMARY KEY (user_id, course_id)
                  );
                  """)

# Handler
fname = input("Enter file name: ")

# If not input provided, use the default one
if len(fname) < 1:
    fname = "roster_data_sample.json"
    
# Open and read the file
str_data = open(fname).read()
# Parse the file
json_data = json.loads(str_data)

# entry is equivalent to each row in the file
for entry in json_data:
    
    # Get the values, asign them to varibles and print what will be inserted into the tables
    name = entry[0]
    title = entry[1]
    print((name, title))
    
    # Insert if the name does not exist in the table
    cur.execute("INSERT OR IGNORE INTO User (name) VALUES (?)", (name, ))
    # Get the id for the name in the line above
    cur.execute("SELECT id FROM User WHERE name = ?", (name, ))
    # Put the id in a variable.
    user_id = cur.fetchone()[0]
    
    # Do the same as lines 53 to 58.
    cur.execute("INSERT OR IGNORE INTO Couse (title) VALUES (?)", (title, ))
    cur.execute("SELECT id FROM Couse WHERE title = ?", (title, ))
    course_id = cur.fetchone()[0]
    
    # Insert the previous two variables into the Member table
    cur.execute("INSERT OR REPLACE INTO Member (user_id, course_id) VALUES (?, ?)", (user_id, course_id))
    
    # Commit changes every time.
    conn.commit()