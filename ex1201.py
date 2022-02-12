"""Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt
There are three ways that you might retrieve this web page and look at the response headers:

Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to change 
the code to retrieve the above URL - the values are different for each URL.
Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
Enter the header values in each of the fields below and press "Submit".
Last-Modified:
ETag:
Content-Length:
Cache-Control:
Content-Type:"""

import socket

# make the socket with a handle
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the site on port 80 using the tuple that contains the domain and the port number
mysock.connect(("data.pr4e.org", 80))
# request method GET to obtain the information and encode is to send the data accross the internet   
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n" .encode()
# Send cmd through mysock
mysock.send(cmd)

# When the server stars sending data back, it is received using this while loop 
while True:
    # The data received via mysock is received by chunks of 512 characters.
    data = mysock.recv(512)
    # if we receive 0 characters, the stream is closed
    if (len(data) < 1):
        break
    # else, if data is received print the decoded data
    print(data.decode())
# close the socket
mysock.close()