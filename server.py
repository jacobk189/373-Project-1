# UDPserver
from socket import *
import sys
serverPort = 12000

#connection_type = input('What type of connection are you running? 1 for UDP 1 connection. 2 for TCP 1 connection. 3 for UDP 5 parallel connections. 4 for TCP 5 parallel connections.\n')
#do some if statments for each input

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind socket to local port number 12000
serverSocket.bind(('', serverPort))
print('server running')
msg, addr = serverSocket.recvfrom(2048)
msg = msg.decode()

fname = 'index.html'

if (msg != fname):
    serverSocket.sendto('404'.encode(), addr)
else:
    serverSocket.sendto('200'.encode(), addr)
    #serverSocket.sendto(fname, addr)

input('enter to close')


