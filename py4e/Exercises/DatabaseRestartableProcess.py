import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl

# Gets the list of friends of a specific account
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# creates sqlite table and handler
conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

# Create tables if they don't exist. The Follows table is to indicata who follows who.
cur.execute('''CREATE TABLE IF NOT EXISTS People
            (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
            (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Do until quit is typed.
while True:
    # Enter the twitter account or quit
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    # If enter is hit with no input, select one non-retrieved contact randomly
    if (len(acct) < 1):
        # Get the id and name
        cur.execute('SELECT id, name FROM People WHERE retrieved=0 LIMIT 1')
        try:
            # In a tuple save the value of the id and name
            (id, acct) = cur.fetchone()
        except:
            # If the value of retrived is 1, it means that the account was already retrieved
            print('No unretrieved Twitter accounts found')
            continue
    # If the name of the contact is provided
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (acct, ))
        try:
            # Grab the id of the selected person
            id = cur.fetchone()[0]
        except:
            # If the person is not in the table, insert it and save.
            cur.execute('''INSERT OR IGNORE INTO People
                        (name, retrieved) VALUES (?, 0)''', (acct, ))
            conn.commit()
            # If no rows were affected, trigger an error
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
            # Grab the id of the selected person
            id = cur.lastrowid

    # Twitter sintax to get the keys and data of the first 100 contacts
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    # Display the name of the account user
    print('Retrieving account', acct)
    try:
        # Open the url variable with the Twitter information
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err:
        print('Failed to Retrieve', err)
        break

    # Read and decode to create a connection.
    data = connection.read().decode()
    # Get the headers in a dictionary
    headers = dict(connection.getheaders())

    # Display the remaining Twitter rate limit
    print('Remaining', headers['x-rate-limit-remaining'])

    try:
        # Load the json data
        js = json.loads(data)
    except:
        print('Unable to parse json')
        print(data)
        break

    # Debugging
    # print(json.dumps(js, indent=4))
    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue

    # Indicate if the account is one of the retrieved accounts
    cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))

    # Go throught all the friends
    countnew = 0
    countold = 0
    for u in js['users']:
        # Get the friend's name
        friend = u['screen_name']
        print(friend)
        # Verify if the person is already in the database
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            # Get the person's id
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            # If the id is new, create the person
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
                        VALUES (?, 0)''', (friend, ))
            conn.commit()
            # Verify how many rows where affected in the previous transacion
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
            # Get the friend id of the last row inserted and add 1 to the count
            friend_id = cur.lastrowid
            countnew = countnew + 1
        # Insert information into the Follows table
        cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id)
                    VALUES (?, ?)''', (id, friend_id))
    print('New accounts=', countnew, ' revisited=', countold)
    # Display the remaining rate limit from Twitter.
    print('Remaining', headers['x-rate-limit-remaining'])
    conn.commit()
cur.close()