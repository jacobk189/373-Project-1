from socket import * #include Python's socket library
import sys

defaultFile = 'index.html'
defaultPort = 12000
defaultName = '127.0.0.1'

if len(sys.argv) == 4:
    print('not enough arguments')
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
    fileName = sys.argv[3]

else:
    serverName = defaultName
    serverPort = defaultPort
    fileName = defaultFile

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(fileName) #will need to add command type ex) GET filename
msg, addr = clientSocket.recvfrom(2048)

if(msg == 200):
    clientSocket.recvfrom(2048)
elif(msg == 404):
    sys.exit()