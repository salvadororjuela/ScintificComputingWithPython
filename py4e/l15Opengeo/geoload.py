import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

# Create the database and cursor
conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

# Create a table that caches the address and geodata 
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
nofound = 0
for line in fh:
    if count > 100 :
        print('Retrieved 100 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    # Use the following statement to pull out the address
    # A memory view is a safe way to expose the buffer protocol in Python. It allows you to 
    # access the internal buffers of an object by creating a memory view object.
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    # The following try except is used to verify if the data already exists in the database.
    try:
        data = cur.fetchone()[0]
        print("Found in database", address)
        continue
    except:
        pass

    parms = dict()
    # Assign the value of the address variable to the q value of the params dictionary
    parms['q'] = address
    # url is a variable that encode the key value pairs of the params dictionary and returns the url address
    # using the format ( http://py4e-data.dr-chuck.net/geojson?query=AGH+University+of+Science+and+Technology)
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    
    ## Retrieve the url, read, decode, and add a count
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    # Parse the data into json and print if something goes wrong
    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    # Verifies if js exists or if the object "features" is present in js
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    # If the features object has a value of 0, inform that the object is not found and add 1 to this count
    if len(js['features']) == 0:
        print('==== Object not found ====')
        nofound = nofound + 1

    # Insert the data into the table in the database
    cur.execute('''INSERT INTO Locations (address, geodata)
                VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()

    # Add a pause of five seconds each tenth one.
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")

