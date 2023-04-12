from socket import * #include Python's socket library
import sys
from html.parser import HTMLParser

defaultFile = 'index.html'
defaultPort = 3905
defaultName = 'compsci04.snc.edu'

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
msg = msg.decode('utf-8')
filedata = ''
if(msg == '200'):
    print('got that bish')
    while(msg != 'done'):
        msg, Serveraddr = clientSocket.recvfrom(2048)
        msg = msg.decode('utf-8')
        filedata = filedata + msg
    print(filedata)
    handledata(filedata)
    input('enter to close')
elif(msg == '404'):
    print('did not find that hoe')
    input('enter to close')
    sys.exit()