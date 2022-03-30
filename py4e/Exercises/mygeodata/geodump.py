"""This program retrieves the information from the Locations table in geodata.sqlite
and inputs it into the where.js file to be displayed on the map in the browser"""
import sqlite3, json, codecs

# Create connection and cursor
conn = sqlite3.connect("geodata.sqlite")
cur = conn.cursor()

# Show all data from the Locations table
cur.execute("SELECT * FROM Locations")
# Open the file where.js in write mode and the wtf-8 format
fhand = codecs.open("where.js", "w", "utf-8")
# Write the file myData
fhand.write("myData = [\n")
count = 0
#Loop through the cursor
for row in cur:
    # Get the element in position #1 and decode 
    data = str(row[1].decode())
    # Convert to string and parse it
    try: js = json.loads(str(data))
    # If something goes wrong skip it
    except: continue
    
    # Check if the status is present in the Locations table or if status is OK
    if not("status" in js and js["status"] == "OK"): continue
    # If status is present or is OK, get lat and lng of each point
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    
    if lat == 0 or lng == 0: continue
    # Get the name of the location which is located in the formated_address attribute
    where = js["results"][0]["formatted_address"]
    # Clean where from '
    where = where.replace("'", "")
    
    try:
        # Display in console the name of the location, lat and lng
        print(where, lat, lng)
        
        count += 1
        if count > 1:
            fhand.write(",\n")
        # Assign the values to the output variable
        output = f"{str(lat)}, {str(lng)}, {where}"
        # Write the value of output in where.js
        fhand.write(output)
    except:
        continue
    
fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "Records written to where.js")
# Indicate the user to open the where.html file to be seen in a browser
print("Open where.html to view the data in a browser")