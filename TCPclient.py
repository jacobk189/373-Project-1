from socket import *
from html.parser import HTMLParser

serverName = 'localhost'
serverPort = 12000
buffer_size = 1024

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for name,value in attrs:
                if name == 'src':
                    print("found one")
                    self.links.append(value)

def handledata(filedata):
    parser = MyHTMLParser()
    parser.feed(filedata)
    links = parser.links
    print(links)

# Get filename from user
filename = input("Enter file name: ")

# Create TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect socket to server
clientSocket.connect((serverName, serverPort))

# Send filename to server
clientSocket.send(filename.encode())

# Receive response from server
response = clientSocket.recv(buffer_size)

if response.decode() == "File not found":
    print("File not found on server")
else:
    print("File found on server")
    filedata = ''
    while True:
        data = clientSocket.recv(buffer_size)
        if not data:
            break
        filedata += data.decode(errors='ignore')
    print(filedata)
    handledata(filedata)

# Close socket
clientSocket.close()