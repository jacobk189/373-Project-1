# UDPserver
from socket import *
import sys
serverPort = 3905
buffer_size = 200

    # Read html file into string
def readHTML(inFile):
	with open(inFile, 'r',encoding='utf-8') as htmlfile:
		data = htmlfile.read()
	return data

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
defaultPort = 3905

if len(sys.argv) == 4:
    serverPort = int(sys.argv[2])
    fileName = sys.argv[3]

else:
    serverPort = defaultPort
    fileName = fname

if (msg != fname):
    serverSocket.sendto('404'.encode(), addr)
else:
    serverSocket.sendto('200'.encode(), addr)
    print("sent 200")
    file_data = readHTML(fname)
    i = 0
    while i < len(file_data):
        if(i+buffer_size<len(file_data)-1):
            msg = file_data[i:i+buffer_size]
        else:
            msg = file_data[i:len(file_data)-1]
        i = i+buffer_size
        serverSocket.sendto(msg.encode('utf-8'), addr)
        print("sent from server: ", msg)
    
    msg = 'done'
    serverSocket.sendto(msg.encode(), addr)
    print("after sent file")
    #serverSocket.sendto(fname, addr)

input('enter to close')

