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