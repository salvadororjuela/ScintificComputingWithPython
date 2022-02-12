"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by 
hour of the day for each of the messages. You can pull the hour out from the 'From ' line by 
finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as 
shown below."""

# open file
fhand = open(input("Enter File:"))
counts = dict()
hours = list()

# iterate over each line of the file
for line in fhand:
    # remove white spaces
    line = line.rstrip()
    # create a list with the words of line
    words = line.split()
    
    # Determine if the line contains at least six words and if the line contains the word "From"
    if len(words) < 6 or "From" not in line:
        continue
    else:
        # if "From" exists in line, get the sixth word
        sixthWord = words[5]
        # get the location of the first colon (:)
        hourLocation = sixthWord.find(":")
        # separate the hour from the first colon, the minutes and the seconds and append it to the hours list
        hours.append(sixthWord[0:hourLocation])

# fill in the counts dictionary with key value pair of the hours and the count of each hour
for hour in hours:
    # set the hours counts. The default value is 0 and each time he hour repeats add 1
    counts[hour] = counts.get(hour, 0) + 1
    
hoursKeyValue = list()
# get a list of the key value pairs in a list of tuples
for hour, count in counts.items():
    # create a tuple per hour, count pair
    tupleHoursCount = (hour, count)
    # add each tupleHoursCount to the hoursKeyValue list
    hoursKeyValue.append(tupleHoursCount)

# print the hoursKeyValue list of tuples sorted from min to max
hoursKeyValue.sort()
for k, v in hoursKeyValue:
    print(k, v)