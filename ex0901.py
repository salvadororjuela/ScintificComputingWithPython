"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent 
the greatest number of mail messages. The program looks for 'From ' lines and takes
the second word of those lines as the person who sent the mail. The program creates a 
Python dictionary that maps the sender's mail address to a count of the number of
times they appear in the file. After the dictionary is produced, the program reads 
through the dictionary using a maximum loop to find the most prolific committer."""

fname = input("Enter file:")
fhand = open(fname)
senders = dict()

# iterate over each line of the document
for line in fhand:
    # remove white spaces 
    line = line.rstrip()
    # split the line and get a list of the words the line contains
    words = line.split()
    # verifies if the line contains at least 1 word and the line contains the word "From"
    if len(words) < 1 or words[0] != "From":
        continue
    
    # Get only the address of senders
    for word in words:
        # get only the email addresses
        if "@" in word:
            # idiom: retreive/create/update counter    
            senders[word] = senders.get(word, 0) + 1

# find the sender who has sent the greatest number of emails
largestSender = -1
thesender = None
# iterate over the key / value pairs of thhe senders dictionary.
for sender, count in senders.items():
    # find the key with the highest value
    if largestSender < count:
        largestSender = count
        thesender = sender # capture/remember the address from where the most emails were sent
        
print(thesender, largestSender)