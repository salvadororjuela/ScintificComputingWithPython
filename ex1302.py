"""Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to 
http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON
data from that URL using urllib and then parse and extract the comment counts from 
the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the 
sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1472949.json (Sum ends with 80)
You do not need to save these files to your folder since your program will read the data 
directly from the URL. Note: Each student will have a distinct data url for the assignment - 
so only use your own data url for analysis.
Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
The closest sample code that shows how to parse JSON and extract a list is json2.py. You
might also want to look at geoxml.py to see how to prompt for a URL and retrieve data
from a URL.

Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2... """

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE 

input = input("Enter location: ")

#  return a single big string line with new lines and the end of each line of the webpage we are looking into
url = urllib.request.urlopen(input, context=ctx).read().decode()
# get the characters length in the url
urlLength = len(url)
# loads json to get the elements
js = json.loads(url)
# get the commets element from the json
comments = js.get("comments")

# variable to sum the value of the count value of each element in the json
counts = 0
sumOfItems = 0
# iterate over the comments using range
for comment in range(len(comments)):
    # get the ith element of the comments variable and turn it into an integer
    count = comments[comment]
    # add the value gotten with the count.get("count") method to the counts variable
    counts += count.get("count")
    # add 1 per iteration to get the number of counts
    sumOfItems += 1
    
print(f"Retrieving {input}")
print(f"Retrieved {urlLength} characters")
print(f"Count: {sumOfItems}")
print(f"Sum: {counts}")