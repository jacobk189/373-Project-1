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
    return links

if len(sys.argv) == 4:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
    fileName = sys.argv[3]

else:
    serverName = defaultName
    serverPort = defaultPort
    fileName = defaultFile

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(fileName.encode('utf-8'), (serverName, serverPort)) #will need to add command type ex) GET filename
msg, Serveraddr = clientSocket.recvfrom(2048)
msg = msg.decode('utf-8')
filedata = ''
clientSocket.settimeout(2)

if(msg == '200'):
    print('got that HTML')
    while(msg != 'done'):
        try:
            msg, Serveraddr = clientSocket.recvfrom(2048)
            msg = msg.decode('utf-8')
            filedata = filedata + msg          
        except timeout:
            break #might lose data? but need in case we miss done

    
    parsedData = handledata(filedata)

    print('making image requests')
    first = True
    for curFile in parsedData:
        clientSocket.sendto(curFile.encode('utf-8'), Serveraddr)
        accumulatedData = b''
        while(1):
            if(first):
                clientSocket.settimeout(None)
                first = False
            else:
                clientSocket.settimeout(0.1)
            try:
                msg, Serveraddr = clientSocket.recvfrom(2048)
                try:
                    msg.decode('utf-8')
                    break   #this is the done message
                except UnicodeDecodeError:
                    accumulatedData = accumulatedData + msg #bytes will not decode properly so add them
            except timeout:
                break
        try:
            file = open(curFile, "wb")
            file.write(accumulatedData)
            file.close() 
        except OSError:
            print('wrong format for: ', curFile)

    clientSocket.sendto('done'.encode('utf-8'), Serveraddr)
    input('done pog enter to close, check image folder')

elif(msg == '404'):
    print('did not find that')
    input('enter to close')
    sys.exit()


        

 