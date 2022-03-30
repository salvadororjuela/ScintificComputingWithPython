from urllib.request import urlopen
import urllib.error 
import twurl
import json
import sqlite3 
import ssl

TWITTER_URL = "https:api.twitter.com/1.1/friends/list.json"

# Connect the database
conn = sqlite3.connect("spider.sqlite")
cur = conn.cursor()

# If the table does not exist it creates it
cur.execute("""CREATE TABLE IF NOT EXISTS Twiter (name TEXT,
            retreieved INTEGER, friends INTEGER)""")

# Ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Loop to continue the iteration or break if quit is typed
while True:
    acct =  input("Enter a Twitter account, or quit: ")
    if (acct == "quit"): break
    # If enter is hit, read from the database an unretrieved Twitter person and grab all that person's friends.
    if (len(acct) < 1):
        cur.execute("SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1")
        try:
            # Get the name of the first person. Get one row from the database, and [0] means get the first colum.
            acct = cur.fetchone()[0]
        except:
            print("No unretieved Twitter account found.")
            continue
        
    url = twurl.augment(TWITTER_URL, {"screen_name": acct, "count": "5"})
    print("Retrieving", url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    
    print("Remaining", headers["x-rate-limit-remainig"])
    js = json.loads(data)
    
    cur.execute("UPDATE Twitter SET retrieved=1 WHERE name = ?", (acct, ))
    
    countnew = 0
    countold = 0
    for u in js["users"]:
        friend = u["screen_name"]
        print(friend)
        cur.execute("SELECT friends FROM Twitter WHERE name = ?", (friend, ))
        
        try:
            count = cur.fetxone()[0]
            cur.execute("UPDATE Twitter SET friends = ? WHERE name = ?", (count+1, friend))
            countold = countold + 1
        except:
            cur.execute("""INSERT INTO Twitter(name, retrieved, friends)
                        VALUES (?, 0, 1)""", (friend, ))
            countnew = countnew + 1
    
    print("New accounts = ", countnew, "revisited = ", countold)
    
cur.close()