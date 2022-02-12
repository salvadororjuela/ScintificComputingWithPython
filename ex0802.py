""" 8.5 Open the file mbox-short.txt and read it line by line. When you find a
line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the
line (i.e. the entire address of the person who sent the message). Then print 
out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at 
the last line of the sample output to see how to print the count.
You can do"""

fname = open(input("Enter file name: "))
emails = list()

for line in fname:
    rstripline = line.rstrip()
    splitline = line.split()
    
    if len(splitline) < 1 or splitline[0] != "From":
        continue 
    
    address = splitline[1]
    print(address)
    emails.append(address)

print(f"There were {len(emails)} lines in the file with From as the first word")
