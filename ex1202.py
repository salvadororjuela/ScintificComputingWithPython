"""Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python
program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read 
the HTML from the data files below, and parse the data, extracting numbers and compute the 
sum of the numbers in the file.
We provide two files for this assignment. One is a sample file where we give you the sum for 
your testing and the other is the actual data you need to process for the assignment.
Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1472946.html (Sum ends with 66)
You do not need to save these files to your folder since your program will read the data 
directly from the URL. Note: Each student will have a distinct data url for the assignment - so 
only use your own data url for analysis."""
    
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# use the following three lines to have access to https sites and add "context=ctx" in line 12 as second parameter in urlopen()
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
# return a signle big string line with new lines at the end of each line of the webpage we are looking into.
html = urllib.request.urlopen(url, context=ctx).read() # context=ctx 
soup = BeautifulSoup(html, "html.parser")

# List to save all values
numbers = list()
# Retrieve all of the anchor tags
tags = soup("span")
for tag in tags:
    # Get the value of each span tag, parse it to an int, and append it to the list numbers
    numbers.append(int(tag.contents[0]))

print(sum(numbers))
    