# Made with <3 by Dan Goodman, signed 12/31/17
# Server

# Code adapted from http://willsrpi.blogspot.co.uk
# and https://stackoverflow.com/questions/9382045/send-a-file-through-sockets-in-python
# and https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist

import socket
from sys import argv
import os

script, argv1, argv2 = argv

print("Checking if a loot folder exists...")
directory = "loot/"
if not os.path.exists(directory):
    print("Loot folder not found! Creating...")
    os.makedirs(directory)
else:
    print("Loot folder exists, continuing...")

print("Waiting for an incoming connection...")
s = socket.socket()
s.bind((str(argv1), int(argv2)))
s.listen(10)
# i=1
sc, addr = s.accept()
print("Client connected...")

while True:
    fileName = sc.recv(1024)
    print("File '{0}' coming from:".format(fileName.decode()), addr)
    f = open("loot/" + fileName.decode(), 'wb')
    # i=i+1
    while True:
        l = sc.recv(1024)
        while l:
            f.write(l)
            l = sc.recv(1024)
            if l == "".encode():
                f.close()
                sc.close()
                print("File '{0}' stuffed in the loot folder, exiting".format(fileName.decode()))
                exit(0)
    f.close()
    sc.close()
