"""Musical Track Database
This application will read an iTunes export file in XML and produce a properly normalized 
database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
If you run the program multiple times in testing or with different files, make sure to 
empty out the data before each run.

You can use this code as a starting point for your application: 
http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml file to be used
for this assignment. You can export your own tracks from iTunes and create a database, but
for the database that you turn in for this assignment, only use the Library.xml data that 
is provided.

To grade this assignment, the program will run a query like this on your uploaded database 
and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
    
The expected result of the modified query on your database is: (shown here as a simple HTML 
table with titles)

Track	Artist	Album	Genre
Chase the Ace	AC/DC	Who Made Who	Rock
D.T.	AC/DC	Who Made Who	Rock
For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock
"""
import sqlite3, xml.etree.ElementTree as ET

# Create db connection
conn = sqlite3.connect("ex1403Trackdb.sqlite")

# Handler 
cur = conn.cursor()

# Create new tables using executescript(). In the Genre table, the DEFAULT "Unknown" is added in case that
# no genre is assigned in Library.xml
cur.executescript("""DROP TABLE IF EXISTS Artist;
                  DROP TABLE IF EXISTS Genre;
                  DROP TABLE IF EXISTs Album;
                  DROP TABLE IF EXISTS Track;
                  
                  CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  name TEXT UNIQUE);
                  
                  CREATE TABLE Genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  name DEFAULT "Unknown" UNIQUE);
                  
                  CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  artist_id INTEGER,
                  title TEXT UNIQUE);
                  
                  CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  title TEXT UNIQUE,
                  album_id INTEGER,
                  genre_id INTEGER,
                  len INTEGER, rating INTEGER, count INTEGER);
                  """)

# Request for a file to open or open the default one
fname = input("Enter file name: ")
if (len(fname) < 1): fname = "Library.xml"

# Function to lookup on object inside object
def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == "key" and child.text == key:
            found = True
    return None

# Parse the string and put it into and XML ET object (stuff)
stuff = ET.parse(fname)
# Find all the third level dictionary because there is a dictionarly inside a dictionary inside a dictionary
all = stuff.findall("dict/dict/dict")
# Display how many objects are contained in the all dictionary
print (f"Dict count: {len(all)}")

# Get the data from the all dictionary
for entry in all:
    # continue if there is no track id
    if (lookup(entry, "Track ID") is None): continue
    # Assign the values inside the all dictionary to a variable
    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    genre = lookup(entry, "Genre")
    len = lookup(entry, "Total Time")
    rating = lookup(entry, "Rating")
    count = lookup(entry, "Play Count")
    
    # Continue if not found. Include previous variables that are possible to be left empty (None)
    if name is None or artist is None or genre is None or album is None: continue
    print(f"""Song: {name}, Artist: {artist}, 
          Album: {album}, Genre: {genre}, 
          Total Time: {len}, Rating: {rating}, 
          File Folder Count: {count}""")
    
    # Insert the artist, if it is already there, don't inster it (OR IGNORE)
    cur.execute("""INSERT OR IGNORE INTO Artist(name) VALUES(?)""", (artist, ))
    # Get the id for each particular artist
    cur.execute("""SELECT id FROM Artist WHERE name = ?""", (artist, ))
    # Fetch the first column that correspond to the artist id
    artist_id = cur.fetchone()[0]

    # Do the same as the previous three lines of code to get the foreign key from the Genre table
    cur.execute("""INSERT OR IGNORE INTO Genre(name) VALUES(?)""", (genre, ))
    cur.execute("""SELECT id FROM Genre WHERE name = ?""", (genre, ))
    # Fetch the first column that correspond to the genre_id
    genre_id = cur.fetchone()[0]

    # Ibidem
    cur.execute("""INSERT OR IGNORE INTO Album(title, artist_id) VALUES(?, ?)""", (album, artist_id ))
    cur.execute("""SELECT id FROM Album WHERE title = ?""", (album, ))
    album_id = cur.fetchone()[0]

    # Insert the values in the connecting table with the many to many relations. If it already exists, replace it.
    cur.execute("""INSERT OR IGNORE INTO Track(title, album_id, genre_id, len, rating, count)
                VALUES(?, ?, ?, ? ,?, ?)""", (name, album_id, genre_id, len, rating, count))

conn.commit()