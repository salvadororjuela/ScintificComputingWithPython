"""8.4 Open the file romeo.txt and read it line by line. For each line, split 
the line into a list of words using the split() method. The program should 
build a list of words. For each word on each line check to see if the word is 
already in the list and if not append it to the list. When the program completes, 
sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt"""


fname = input("Enter file name: ")
fh = open(fname)
# List to store
lst = list()
# loop each line of lst
for line in fh:
    # remove right extra blank spaces
    line = line.rstrip()
    # separate each word of each line
    words = line.split()
    # verify if the the word is not already present in the words list
    for word in words:
        if word not in lst:
            # if word is not present append it in lst
            lst.append(word)
lst.sort()
print(lst)