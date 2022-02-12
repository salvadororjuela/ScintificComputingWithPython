import re
hand = open("mbox-short.txt")

# Using re.search() like find()
for line in hand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)
   
# Using re.search() like startswith()     
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line)
   
# Matching and Extracting Dta
x = "My 2 favorite numbers are 20 and 23"
y = re.findall("[0-9]+", x)
z = re.findall("[AEIOU]+", x)
print(y) 
print(z)

# greedy matching
a = "From: Using the : character"
b = re.findall("^F.+:", a)
c = re.findall("^F.+?:", a)
print("Greedy matching will use the largest possible string as follows:", b, "\n")
print("Non-greedy matching will use the shorter:", c, "\n")

# Fine-tunning String Extraction
senderInfo = "From example@ufc.com.uk Sun Jan 6 08:07:09 2000"
email = re.findall("\S+@\S+", senderInfo)
print(f"Get the email: {email}\n")

# A more specific search with the same previous result
emailRefined = re.findall("^From (\S+@\S+)", senderInfo) # this will find the lines that start with "From" but will return only the part inside parenthesis
print(f"Get the email from lines that start with 'From': {emailRefined}\n")

# another more precisce method. This time includes the lines that start with "From", but only gets the characters after @ and before the white space.
emailPrecise = re.findall("^From .*@([^ ]*)", senderInfo)
print(f"A more precise method to the only the characters after the '@' and before the blank space: {emailPrecise}\n")

# test
import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst, "\n")

# spam confidence
fhand = open("mbox-short.txt")
numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print(f"Maximum: {max(numlist)}\n")

# escape character
sentence = "We just received $10.10 for cookies."
searchPatern = re.findall("\$[0-9.]+", sentence)
print(searchPatern)