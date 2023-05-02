from socket import *

serverPort = 12000
buffer_size = 1024

# Read html file into string
def readHTML(inFile):
    with open(inFile, 'r', encoding='utf-8') as htmlfile:
        data = htmlfile.read()
    return data

# Create TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind socket to local port number
serverSocket.bind(('', serverPort))
print('server running')

# Listen for incoming connections
serverSocket.listen(1)

while True:
    # Accept incoming connection
    connectionSocket, addr = serverSocket.accept()
    print("Connection from ", addr)

    # Receive filename from client
    filename = connectionSocket.recv(buffer_size).decode()

    # Check if file exists
    try:
        filedata = readHTML(filename)
        connectionSocket.send("File found".encode())
        print("File found")
        i = 0
        while i < len(filedata):
            msg = filedata[i:i+buffer_size]
            connectionSocket.send(msg.encode())
            i += buffer_size
        print("File sent")
    except FileNotFoundError:
        connectionSocket.send("File not found".encode())
        print("File not found")

    # Close connection
    connectionSocket.close()