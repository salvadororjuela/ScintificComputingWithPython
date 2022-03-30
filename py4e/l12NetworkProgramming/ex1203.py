"""Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the
anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow 
that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing 
and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer
is the last name that you retrieve.

Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Shannah.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer
is the last name that you retrieve.

Hint: The first character of the name of the last page that you will load is: T
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult 
for you to do the assignment without writing a Python program. But frankly with a little effort and patience 
you can overcome these attempts to make it a little harder to complete the assignment without writing a Python 
program. But that is not the point. The point is to write a clever Python program to solve the program.

Sample execution

Here is a sample execution of a solution:

$ python3 solution.py
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
The answer to the assignment for this execution is "Anayah"."""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# use the following three lines to have access to https sites and add "context=ctx" in line 12 as second parameter in urlopen()
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
count = int(input("Enter count:"))
position = int(input("Enter position:"))

print(url)

# follow the link the number of times indicated in the count variable
for i in range(count):
    # return a signle big string line with new lines at the end of each line of the webpage we are looking into.
    html = urllib.request.urlopen(url, context=ctx).read() # context=ctx 
    soup = BeautifulSoup(html, "html.parser")
    # list to store all links in the anchor tags. It is cleared on each iteration, except on the last one.
    links = list()
    # list to store all authors' names. It is cleared on each iteration, except on the last one.
    names = list()
    # Retrieve all of the anchor tags
    tags = soup("a")
    for tag in tags:
        # populate the links list with the anchor tags
        links.append(tag.get("href", None))
        # populate the names list with the content of the tag
        names.append(tag.contents[0])

    # Store the link located in the position indicated by the user. 
    theChosenLink = links[position -1]
    # replace the value of the url varible with the value of the theChosenLink varible to iterate over the new value every time
    url = theChosenLink
    print(theChosenLink)

# print the name of the author of the last url
print(f"Author's name: {names[position - 1]}")