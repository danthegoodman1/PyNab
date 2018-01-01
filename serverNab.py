# Made with <3 by Dan Goodman, signed 12/31/17
# Server

# Code adapted from http://willsrpi.blogspot.co.uk
# and https://stackoverflow.com/questions/9382045/send-a-file-through-sockets-in-python
# and https://stackoverflow.com/questions/19412029/transfering-file-over-tcp-using-python

import socket
from sys import argv

script, argv1, argv2 = argv
#
# host = str(argv1)
# port = int(argv2)
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))
# s.listen(1)
# conn, addr = s.accept()
# print ("Connection from", addr)
# while True:
#     data = conn.recv(1024)
#     if not data:
#         break
#
#     print("Recieved: "+(data))
#     response = raw_input("Reply: ")
#     if response == "exit":
#         break
#
#     conn.sendall(response)
# conn.close()
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
    f = open(fileName.decode(),'wb')
    # i=i+1
    while True:
        l = sc.recv(1024)
        while l:
            f.write(l)
            l = sc.recv(1024)
            if l == "".encode():
                f.close()
                sc.close()
                print("File '{0}' received, exiting".format(fileName.decode()))
                exit(0)
    f.close()
    sc.close()
