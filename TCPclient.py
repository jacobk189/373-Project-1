from socket import * #include Python's socket library
import sys
from html.parser import HTMLParser

defaultFile = 'index.html'
defaultPort = 3905
defaultName = '127.0.0.1' #'compsci04.snc.edu'

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
    #print(links)
    return links

if len(sys.argv) == 4:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
    fileName = sys.argv[3]

else:
    serverName = defaultName
    serverPort = defaultPort
    fileName = defaultFile

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

clientSocket.send(fileName.encode('utf-8')) #will need to add command type ex) GET filename
msg = clientSocket.recv(2048)
msg = msg.decode('utf-8')
filedata = ''

if(msg == '200'):
    print('got that HTML')
    msg = ''  
    while 'OURPASSWORDCODE' not in msg:
        msg = clientSocket.recv(2048)
        msg = msg.decode('utf-8')
        filedata = filedata + msg
        print(msg,'\n')

    parsedData = handledata(filedata)
    print('making image requests')

    for curFile in parsedData:
        clientSocket.send(curFile.encode('utf-8'))
        accumulatedData = b'' 

        while(1):
            msg = clientSocket.recv(2048)
            try:
                msg.decode('utf-8')
                break   #this is the done message
            except UnicodeDecodeError:
                accumulatedData = accumulatedData + msg #bytes will not decode properly so add them
        try:
            file = open(curFile, "wb")
            file.write(accumulatedData)
            file.close()
        except OSError:
            print('wrong format for: ', curFile)      

    clientSocket.send('OURPASSWORDCODE'.encode('utf-8'))
    input('done pog enter to close, check image folder')

    clientSocket.close()

elif(msg == '404'):
    print('did not find that')
    input('enter to close')
    sys.exit()

                



