# UDPserver
from socket import *
import sys
serverPort = 12000

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind socket to local port number 12000
serverSocket.bind(('', serverPort))


# Loop forever
while i<num:
	# Read from UDP socket into message, getting client's 
	# address (client IP and port)
	#modifiedMessage = message.decode().upper()
	
	serverSocket.sendto(madlibwords[i].encode(), clientAddress)
	
	
	#send upper case string back to this client
	#serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    #this is me adding something jackson