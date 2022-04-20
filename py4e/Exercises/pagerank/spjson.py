"""Program to visualize the information using a javascript file (force.js) that feeds in 
the visualization program(d3.v2.js). This occurs when this file creates a json file that is 
the source of information to visualize"""

import sqlite3

conn = sqlite3.connect("spider.sqlite")
cur = conn.cursor()

print("Creating JSON ouput on spider.js...")
howmany = int(input("How many nodes?"))

# Get the information from the tables usign a join
cur.execute("""SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url
            FROM Pages JOIN Links on Pages.id = Links.to_id
            WHERE html IS NOT NULL AND ERROR IS NULL
            GROUP BY id ORDER BY id, inbound""")

fhand = open("spider.js", "w")
nodes = list()
maxrank = None 
minrank = None 
# read through all the rows and...
for row in cur:
     nodes.append(row)
     # ...pull out the page rank.
     rank = row[2]
     # Get the minimum rank and maximum rank.
     if maxrank is None or maxrank < rank: maxrank = rank
     if minrank is None or minrank > rank: minrank = rank
     if len(nodes) > howmany: break
     
# Check the database to verify if there is information in it. If not, the user is prompted to run sprank.py
if maxrank == minrank or maxrank is None or minrank is None:
    print("Error - Please run sprank.py to compute page rank")
    quit()

# Write on the JavaScript file   
fhand.write("spiderJson = {'nodes':[\n")
count = 0
map = dict()
ranks = dict()
for row in nodes:
    if count > 0 : fhand.write(",\n")
    # print row. Normalize the rank and write it out in the JavaScript file.
    rank = row[2]
    rank = 19 * ((rank - minrank) / (maxrank - minrank))
    fhand.write('{' + '"weight":' + str(row[0]) + ',"rank":' + str(rank) + ',')
    fhand.write('"id":' + str(row[3]) + ', "url":"' + row[4] + '"}')
    map[row[3]] = count
    ranks[row[3]] = rank
    count = count + 1
fhand.write('],\n')

cur.execute("SELECT DISTINCT from_id, to_id FROM Links")
fhand.write('"links": [\n')

count = 0
for row in cur:
    # print row
    if row[0] not in map or row[1] not in map: continue
    if count > 0: fhand.write(',\n')
    rank = ranks[row[0]]
    srank = 19 * ((rank - minrank) / (maxrank - minrank))
    fhand.write('{"source": ' + str(map[row[0]]) + ',"target":' + str(map[row[0]]) +', "value":3}')
    count = count + 1
    
fhand.write(']};')
fhand.close()
cur.close()

print("Open force.html in a browser to view the visualization")