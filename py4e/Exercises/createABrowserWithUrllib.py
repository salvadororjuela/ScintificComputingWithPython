import urllib.request, urllib.parse, urllib.error # import urllib necesary modules

####################################################################################################
# READING WEB PAGES
# get, encode and retreive the headers from the conection. Finally it returns and file handle like object
# to be used in the following loop
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
print("\n")

for line in fhand:
    print(line.decode().strip())
print("\n")
    
#############################################################################################
# treat the web page Like a file and get a count of each word

fhandle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
# dictionary to store the words from the web page
counts = dict()
for line in fhandle:
    # as line is bytes and not string, it is necesary to decode it and split it
    words = line.decode().split()

    for word in words:
        # get each word and add a tupple to the counts dictionary with the word and the count of each word
        counts[word] = counts.get(word, 0) + 1
print(counts, "\n")
