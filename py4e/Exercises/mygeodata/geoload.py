import http, sqlite3, json, time, ssl, sys
import urllib.request, urllib.parse, urllib.error

api_key = False
# If you have a Google Places API key, enter it here
# api_key = "AizaSy__________"

# Verifies if an API key is provided or uses the suggested url to retrieve the data
if api_key is False: 
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    
# Create the database
conn = sqlite3.connect("geodata.sqlite")
cur = conn.cursor()

# Create a table that caches the address and geodata
cur.execute("CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)")

# Ignore SSE certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Open the where.data 
fh = open("where.data")
# Loop through the file 200 times
count = 0
for line in fh:
    if count > 200:
        print("Retrieved 200 locations, restart to retrieve more")
        break
    
    # Pull out the address from the line
    address = line.strip()
    print('')
    # Use the following statement to pull out the address
    # A memory view is a safe way to expose the buffer protocol in Python. It allows you to 
    # access the internal buffers of an object by creating a memory view object.
    cur.execute("SELECT geodata FROM Locations WHERE address = ?", (memoryview(address.encode()), ))
    
    # The following try except is used to verify if the data already exists in the database.
    try:
        data = cur.fetchone()[0]
        print("Found in database ", address)
        continue
    except:
        pass
    
    params = dict()
    # Assign the value of the address variable to the query value of the params dictionary
    params["query"] = address
    # Assign the value of api_key to the key of the dictionary
    if api_key is not False: params["key"] = api_key
    # url is a variable that encode the key value pairs of the params dictionary and returns the url address
    # using the format ( http://py4e-data.dr-chuck.net/geojson?query=AGH+University+of+Science+and+Technology)
    url = serviceurl + urllib.parse.urlencode(params)
    
    print(f"Retreiving {url}")
    
    # Retrieve the url, read, decode, and add a count
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count += 1
    
    # Parse the data into json and print if something goes wrong
    try: 
        js = json.loads(data)
    except:
        print(data) # We print in case unicode causes an error
        continue
    
    # Inside js there is a "status" object. The following condition evaluates if this objects exists in js on each iteration
    if "status" not in js or (js["status"]) != "OK" and js["status"] != "ZERO_RESULTS":
        print("=======Failure to Retrieve===========")
        print(data)
        break
    
    # Insert the data into the table in the database
    cur.execute("INSERT INTO Locations (address, geodata) VALUES (?, ?)", (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()
    
    # Add a pause of five seconds each tenth one.
    if count % 10 == 0:
        print("Pausint for a bit...")
        time.sleep(5)
    
print("Run geodump.py to read the data from the database so you can vizualize it on a map.")