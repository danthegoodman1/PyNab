# Made with <3 by Dan Goodman, signed 12/31/17
# Client

# Code adapted from http://willsrpi.blogspot.co.uk
# and https://stackoverflow.com/questions/9382045/send-a-file-through-sockets-in-python
# and https://stackoverflow.com/questions/19412029/transfering-file-over-tcp-using-python

import socket
from sys import argv

script, argv1, argv2, argv3 = argv

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((str(argv1), int(argv2)))
# print("Connected to " + (host) + " on port " + str(port))
# initialMessage = raw_input("Send: ")
# s.sendall(initialMessage)

fileName = ""

# Gotta make sure we don't make crazy nested folders!
# This will make sure to only send the file name, not the whole path.
for i in range(0, len(str(argv3))):
    if "/" in str(argv3):
        x = -1
        while fileName == "":
            if argv3[x] == "/":
                fileName = argv3[(x + 1):]
            else:
                x -= 1
    else:
        fileName = str(argv3)

# Now we send the file name first for easy file name creation on the server side
s.sendall(fileName.encode())

f = open(argv3, "rb")
data = f.read()

# s.sendfile(argv3)

f = open(str(argv3), "rb")
l = f.read(1024)
while l:
    s.send(l)
    # Every time we read again we get the next 1024 bytes
    l = f.read(1024)
s.close()