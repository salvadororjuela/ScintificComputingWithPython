import xml.etree.ElementTree as ET
import sqlite3

# Crate db connection
conn = sqlite3.connect("trackdb.sqlite")
# Handler
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript("""DROP TABLE IF EXISTS Artist;
                  DROP TABLE IF EXISTS Album;
                  DROP TABLE IF EXISTS Track;
                  
                  CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  NAME TEXT UNIQUE);
                  
                  CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  artist_id INTEGER,
                  title TEXT UNIQUE);
                  
                  CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  title TEXT UNIQUE,
                  album_iD INTEGER,
                  len INTEGER, rating INTEGER, count INTEGER);
                   """)

# File
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# Function to lookup on object inside of the object
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# Parse the string and put it into an XML ET object (stuff)
stuff = ET.parse(fname)
# Find all the third level dictionary because there is a dicitonary inside a dictionary inside a dictionary
all = stuff.findall("dict/dict/dict")
# How many things are there in the file
print("Dict count: ", len(all))

# entry will iterate over each of the things
for entry in all:
    # continue if there is no track id
    if(lookup(entry, "Track ID") is None): continue
    # Assign the values inside to a variable
    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    count = lookup(entry, "Play Count")
    rating = lookup(entry, "Rating")
    length = lookup(entry, "Total Time")
    
    # Continue if not found
    if name is None or artist is None or album is None:
        continue
    
    print(name, artist, album, count, rating, length)
    
    # Insert the artist. If it is already there, don't insert it (OR IGNORE)
    cur.execute("""INSERT OR IGNORE INTO Artist(name) VALUES(?)""", (artist, ))
    # Get the id for each particular Artist
    cur.execute("""SELECT id FROM Artist WHERE name = ?""", (artist, ))
    # Fetch the first row that correspond to the artist id
    artist_id = cur.fetchone()[0]
    
    # Do the same as the previous three lines of code to get the foreign key from the Album table (artist_id)
    cur.execute("""INSERT OR IGNORE INTO Album(title, artist_id) VALUES(?, ?)""", (album, artist_id))
    cur.execute("""SELECT id FROM Album WHERE title = ?""", (album, ))
    album_id = cur.fetchone()[0]
    
    # Insert the information. If already exists, replace it. 
    cur.execute("""INSERT OR REPLACE INTO Track(title, album_id, len, rating, count) 
                VALUES(?, ?, ?, ?, ?)""", (name, album_id, length, rating, count))
    
    conn.commit()


"""Commands to run in DB Browser
SELECT Track.title, Album.title, Artist.name FROM Track JOIN Album JOIN Artist ON Track.album_id = Album.id AND Album.artist_id = Artist.id"""