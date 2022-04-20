"""This program updates the rank of each page everytime is run"""
import sqlite3

# Create the database and cursor
conn = sqlite3.connect("spider.sqlite")
cur = conn.cursor()

# Find the ids that send out page rank - we only are interedted
# in pages in the SCC that have in and out links
# Fill in the from_ids list with unique from_id links. So no duplicates are stored in it
cur.execute("""SELECT DISTINCT from_id FROM Links""")
from_ids = list()
for row in cur:
    from_ids.append(row[0])
    
# Find the ids that receive page rank
to_ids = list()
links = list()
cur.execute("SELECT DISTINCT from_id, to_id FROM Links")
for row in cur:
    from_id = row[0]
    to_id = row[1]
    if from_id == to_id: continue
    if from_id not in from_ids: continue 
    if to_id not in from_ids: continue 
    links.append(row)
    # Append only strongly connected components
    if to_id not in to_ids: to_ids.append(to_id)

# Get the latest page ranks for strongly connected components
prev_ranks = dict()
for node in from_ids:
    cur.execute("SELECT new_rank FROM Pages WHERE id = ?", (node, ))
    row = cur.fetchone()
    # We will stick to a dictionary  the new ranks based on the id.
    prev_ranks[node] =  row[0]
 
# Ask for the number of iterations and make an integer of that   
sval = input("How many iterations? ")
many = 1
if (len(sval) > 0): many = int(sval)

# Make a sanity check in case there are no values in the prev_rank column
if len(prev_ranks) < 1 : 
    print("Nothing to page rank. Check data.")
    quit()
    
# Do a Page Rank in memory so it is fast. To do so, it is necessary to compute the new
# page ranks
for i in range(many):
    next_ranks = dict()
    total = 0.0
    for (node, old_rank) in list(prev_ranks.items()):
        total = total + old_rank
        next_ranks[node] = 0.0
        
    # Find the number of outbound links and send the page rank down each
    for (node, old_rank) in list(prev_ranks.items()):
        # Print node, old_rank
        give_ids = list()
        for (from_id, to_id) in links:
            if from_id != node: continue
            # print '   ', from_id, to_id
            
            # Calculation to get the average
            if to_id not in to_ids: continue
            give_ids.append(to_id)
        if (len(give_ids) < 1 ): continue
        amount = old_rank / len(give_ids)
        
        # Calculation to get the value to the new value of the rank to each id
        for id in give_ids:
            next_ranks[id] = next_ranks[id] + amount
    
    # Get the new totals to each id        
    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank
    evap = (total - newtot) / len(next_ranks)
    
    # Print newtot, evap
    for node in next_ranks:
        next_rank[node] = next_ranks[node] + evap
        
    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank
    
    # Compute the per-page averaghe change from old rank to new rank
    # As indication of convergence of the algorithm
    # All this caculations are to show the average difference between page ranks
    totdiff = 0
    for (node, old_rank) in list(prev_ranks.items()):
        new_rank = next_ranks[node]
        diff = abs(old_rank - new_rank)
        totdiff = totdiff + diff
        
    # This is goint to tell us the stability of the page rank.
    # Between each iteration the more it changes, the less stable it is.
    # Average difference in the page ranks per node
    avediff = totdiff / len(prev_ranks)
    print(i + 1, avediff)
        
    # Take the new ranks and make them the old ranks
    prev_ranks = next_ranks
    
    # Put the final ranks back into the database
    print(list(next_ranks.items())[:5])
    cur.execute("UPDATE Pages SET old_rank=new_rank")
    for (id, new_rank) in list(next_ranks.items()):
        cur.execute("UPDATE Pages SET new_rank=? WHERE id = ?", (new_rank, id))
    
    conn.commit()
    cur.close()