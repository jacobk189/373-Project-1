from socket import *
import sys
import time


serverPort = 12000
buffer_size = 1024

# Read html file into string
def readHTML(inFile):
    with open(inFile, 'r', encoding='utf-8') as htmlfile:
        data = htmlfile.read()
    return data

fname = 'index.html'
defaultPort = 3905

if len(sys.argv) == 4:
    serverPort = int(sys.argv[2])
    fileName = sys.argv[3]

else:
    serverPort = defaultPort
    fileName = fname

# Create TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind socket to local port number
serverSocket.bind(('', serverPort))
print('server running')

# Listen for incoming connections
serverSocket.listen(1)
connectionSocket, address = serverSocket.accept()
msg = connectionSocket.recv(2048)

msg = msg.decode('utf-8')


if (msg != fname):
    connectionSocket.send('404'.encode('utf-8'))
else:
    connectionSocket.send('200'.encode('utf-8'))
    print("sent 200")
    file_data = readHTML(fname)
    i = 0

    while i < len(file_data):
        if(i+buffer_size<len(file_data)):
            msg = file_data[i:i+buffer_size]
        else:
            msg = file_data[i:len(file_data)]

        i = i+buffer_size
        connectionSocket.send(msg.encode('utf-8'))
        print("sent from server: ", msg)

    msg = 'OURPASSWORDCODE'
    connectionSocket.send(msg.encode('utf-8'))
    print("after sent file")

    while (1):
        msg = connectionSocket.recv(2048)
        msg = msg.decode('utf-8')
        print('first message of image requests: ', msg)
        if 'OURPASSWORDCODE' in msg:
            break
        try:
            addPath = './server_files'
            actualPath = addPath + msg[1:len(msg)] # this part is only needed for testing on local
            print(actualPath)
            imgFile = open(actualPath,"rb")
            #imgFile = open(msg,"rb")   this is for compsci04
            imgData = imgFile.read()
            i = 0
            while i < len(imgData):
                if(i+buffer_size<len(imgData)):
                    msg = imgData[i:i+buffer_size]
                else:
                    msg = imgData[i:len(imgData)]
                i = i+buffer_size
                #print(msg)
                connectionSocket.send(msg)
                print('sending ', imgFile, '\n')
            connectionSocket.send('done'.encode('utf-8'))    
        except FileNotFoundError: 
            connectionSocket.send('done'.encode('utf-8'))

connectionSocket.close()
input('done pog enter to close')