"""This program gets the links from a webpage, and inserts them into the tables
in the database. """
import sqlite3, urllib.error, ssl
# The following three imports are nececary to read url's
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen 
from bs4 import BeautifulSoup 

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create the database and connection with the cursor
conn = sqlite3.connect("spider.sqlite")
cur = conn.cursor()

# Create the tables in database
cur.execute("""CREATE TABLE IF NOT EXISTS Pages
            (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
            error INTEGER, old_rank REAL, new_rank REAL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS Links
            (from_id INTEGER, to_id INTEGER)""")

cur.execute("""CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)""")

# html IS NULL is used to indicate if the page is not yet been retrieved
# ORDER BY RANDOM() LIMIT 1 means randomly pick a record from the database where html and error IS NULL
cur.execute("SELECT id, url FROM Pages WHERE html IS NULL AND error IS NULL ORDER BY RANDOM() LIMIT 1")
# Fetch the row and verify...
row = cur.fetchone()
# If the web is already in the data base, request to remove it
if row is not None:
    print("Restarting existing crawl. Remove spider.sqlite to start a fresh crawl.")
# Else if the row does not contain information, ask for a new web and insert it.
else:
    starturl = input("Enter web url or hit enter: ")
    if ( len(starturl) < 1) : starturl = "http://www.dr-chuck.com/"
    if ( starturl.endswith("/") ) : starturl = starturl[:-1]
    web = starturl
    if ( starturl.endswith(".htm") or starturl.endswith(".html")):
        pos = starturl.rfind("/")
        web = starturl[:pos]
        
    if (len(web) > 1):
        # Inserts the url into the Webs table without the "/" at the end
        cur.execute("INSERT OR IGNORE INTO Webs (url) VALUES (?)", (web, ))
        # Insert the url into the Pages table without the "/" and adds NULL to html column and 1 to the new_rank
        cur.execute("INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, NULL, 1.0)", (starturl, ))
        
# Get the current webs and store this data into a list (webs)
cur.execute("SELECT url FROM Webs")
webs = list()
for row in cur:
    webs.append(str(row[0]))
    
print(webs)

# Loop to ask for how many pages and break if value is less than 1
many = 0
while True:
    if (many < 1):
        sval = input("How many pages?: ")
        if (len(sval) < 1): break
        many = int(sval)
    many = many - 1
    
    # Look for a NULL page ordered by a random limited to 1
    cur.execute("SELECT id, url FROM Pages WHERE html IS NULL AND error IS NULL ORDER BY RANDOM() LIMIT 1")
    # Grab the content fromid which is the page we are linking from and the url
    try:
        row = cur.fetchone()
        # Print row
        fromid = row[0]
        url = row[1]
    except:
        print("No unretrieved HTML pages found")
        many = 0
        break

    print(fromid, url, end=" ")
    
    # If we are retrieving this page, there should be no links from it
    cur.execute("DELETE FROM Links WHERE from_id = ?", (fromid, ))
    try:
        document = urlopen(url, context=ctx)
        
        html = document.read()
        # Check for the error code, if there is an error update Pages so that error is not retrieved again
        if document.getcode() != 200:
            print("Error on page: ",document.getcode())
            cur.execute("UPDATE Pages SET error=? WHERE url=?", document.getcode(), url)
            
        # Check if the content is different from text/html
        if "text/html" != document.info().get_content_type():
            print("Ignore non text/html page")
            # Delete any non text/http content 
            cur.execute("DELETE FROM Pages WHERE url=?", (url, ))
            cur.execute("UPDATE Pages SET error=0 WHERE url=?", (url, ))
            conn.commit()
            continue
        
        # Print how many characters there are.
        print('('+str(len(html))+')', end= " ")
        
        # Parse with Beautiful Soup
        soup = BeautifulSoup(html, "html.parser")
    
    # If the error is produced by keyboard interruption (CTRL + C)  
    except KeyboardInterrupt:
        print("")
        print("Program interrupted by user...")
        break
    
    # Other errors
    except:
        print("Unable to retrieve or parse the page.")
        cur.execute("UPDATE Pages SET error=-1 WHERE url = ?", (url, ))
        conn.commit()
        continue
            
    # At this point we already got the html for the url, and we proceed to insert it along 
    # with value of 1.0 to the page rank
    cur.execute("INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, NULL, 1.0)", (url, ))
    # In case the page is already there update the information
    cur.execute("UPDATE Pages SET html = ? WHERE url = ?", (memoryview(html), url, ))
    
    # Retrieve all of the anchor tags
    tags = soup("a")
    count = 0
    for tag in tags:
        href = tag.get("href", None)
    
        # The following parse uses the urlparse library to parse the url and break it into pieces
        # Resolve relative references like href="/contact"
        up = urlparse(href)
        if (len(up.scheme) < 1):
            # Hooks up url and href
            href = urljoin(url, href)
            
        # Checks for anchors 
        ipos = href.find("#")
        # Throw everything after the anchor away
        if (ipos > 1 ) : href = href[:ipos]
        # If any of the following extentions are found, continue
        if (href.endswith(".png") or href.endswithd(".jpg") or href.endswith(".gif")): continue
        # If a slash is found at the end, remove it.
        if (href.endswith("/")) : href = href[:-1]
        if (len(href) < 1 ): continue
        
        # Check if the URL is in any of the webs
        found = False
        for web in webs:
            if (href.startswith(web)):
                found = True
                break
        
        # If the link leaves the sites, skip it    
        if not found: continue
        
        # Put into Pages url, null for html because it has not been retrieved yet, and the new rank of 1.0
        cur.execute("INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, NULL, 1.0)", (href, ))
        count += 1
        conn.commit()
        # Get the id and insert it into the Links table
        cur.execute("SELECT id FROM Pages WHERE url = ? LIMIT 1", (href, ))
        try: 
            row = cur.fetchone()
            toid = row[0]
        except:
            print("Could not retrieve the id")
            continue
        
        # Print fromid, toid
        cur.execute("INSERT OR IGNORE INTO Links (from_id, to_id) VALUES (?, ?)", (fromid, toid))
    
    print(count)

cur.close()
    
    