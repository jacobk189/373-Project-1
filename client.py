from socket import * #include Python's socket library
import sys

defaultFile = 'index.html'
defaultPort = 3509
defaultName = '138.74.63.8'

def parse(data):
    arr = str(data).split('href=')
    print(arr)

if len(sys.argv) == 4:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
    fileName = sys.argv[3]

else:
    serverName = defaultName
    serverPort = defaultPort
    fileName = defaultFile

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(fileName.encode(), (serverName, serverPort)) #will need to add command type ex) GET filename
msg, Serveraddr = clientSocket.recvfrom(2048)
msg = msg.decode()
filedata = ''
if(msg == '200'):
    print('got that bish')
    while(msg != 'done'):
        msg, Serveraddr = clientSocket.recvfrom(2048)
        msg = msg.decode()
        filedata+=msg
    parse(filedata)
    input('enter to close')
    #clientSocket.recvfrom(2048)
elif(msg == '404'):
    print('did not find that hoe')
    input('enter to close')
    sys.exit()