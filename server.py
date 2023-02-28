# UDPserver
from socket import *
import sys
serverPort = 12000

#connection_type = input('What type of connection are you running? \n')
#do some if statments for each input

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind socket to local port number 12000
serverSocket.bind(('', serverPort))
