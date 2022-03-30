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

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
    
# http://www.dr-chuck.com/page1.htm
# https://www.si.umich.edu/