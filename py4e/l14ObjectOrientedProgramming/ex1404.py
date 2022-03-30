"""Instructions
This application will read roster data in JSON format, parse the file, and then produce an SQLite
database that contains a User, Course, and Member table and populate the tables from the data file.

You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py - this code 
is incomplete as you need to modify the program to store the role column in the Member table to
complete the assignment.

Each student gets their own file for the assignment. Download this file and save it as 
roster_data.json. Move the downloaded file into the same folder as your roster.py program.

Once you have made the necessary changes to the program and it has been run successfully reading
the above JSON data, run the following SQL command:

SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
The output should look as follows:

Zoubaeir|si422|0
Zi|si334|0

Once that query gives the correct data, run this query:

SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
You should get one row with a string that looks like XYZZY53656C696E613333."""

import sqlite3, json

# Create the database and connect to it
conn = sqlite3.connect("ex1404Rooster.sqlite")
# Create the cursor to handle the database
cur = conn.cursor()

# Create the tables in the database using executescript to run all the senteces.
cur.executescript("""
                DROP TABLE IF EXISTS User;
                DROP TABLE IF EXISTS Course;
                DROP TABLE IF EXISTS Member;
            
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
fhand = input("Enter file name: ")
# If no input provided use the default one
if len(fhand) < 1:
    fhand = "roster_data.json"

# Open, read, and parse the file
json_data = json.loads(open(fhand).read())

# Iterate over each row of the file in the json_data variable
for row in json_data:
    # Get the values and assigned to variables
    name = row[0]
    course = row[1]
    role = row[2]
    print(f"name: {name}, course: {course}, role: {role}")
    
    # Insert the name into the Users database if it does not exist
    cur.execute("""INSERT OR IGNORE INTO User(name) VALUES(?)""", (name, ))
    # Get the value of the user_id property to use it later in a primary-foreign key logical relation
    cur.execute("""SELECT id FROM User WHERE name = ?""", (name, ))
    # Store the value of the user_id property into a variable 
    user_id = cur.fetchone()[0]
    
    # Ibidem
    cur.execute("""INSERT OR IGNORE INTO Course(title) VALUES(?)""", (course, ))
    cur.execute("""SELECT id FROM Course WHERE title = ?""", (course, ))
    course_id = cur.fetchone()[0]
    
    # Insert the previous variables into the Members table.
    current = cur.execute("""INSERT OR REPLACE INTO Member(user_id, course_id, role)
                VALUES (?, ?, ?)""", (user_id, course_id, role))
    
# Commit changes after all data is processed
conn.commit()