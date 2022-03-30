"""Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract 
all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your 
testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_1472944.txt (There are 77 values and the sum ends with 403)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your 
Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis."""


import re

fhand = open("regex_sum_1472944.txt")
# fhand = open("regex_sum_42.txt")
count = 0
# use read method to get all lines of the file
numbers = fhand.read()
# regex to identify the numbers inside the document stored in the list of characters "numbers"
numbersFound = re.findall("[0-9]+", numbers)
# list to store all numbers
numsList = list()

# iterate over numbersFound
for num in numbersFound:
    # convert each value of numberFound into an integer
    number = int(num)
    # append each integer to the numsList list
    numsList.append(number)
    count += 1

print(numsList)
print(count)
print(sum(numsList))