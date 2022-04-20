import sqlite3

# create database and cursor
conn = sqlite3.connect("spider.sqlite")
cur = conn.cursor()

# Information to select ordered in descending order
cur.execute("""SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url
            FROM Pages JOIN Links ON Pages.id = Links.to_id
            WHERE html IS NOT NULL
            GROUP BY id ORDER BY inbound DESC""")

# Get the first 50 rows with the most inbound links from the cur and print it
count = 0 
for row in cur:
    if count < 50: print(row)
    count = count + 1
    
print(count, "rows.")
cur.close()