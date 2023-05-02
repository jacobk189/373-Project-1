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

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(fileName.encode('utf-8'), (serverName, serverPort)) #will need to add command type ex) GET filename
msg, Serveraddr = clientSocket.recvfrom(2048)
msg = msg.decode('utf-8')
filedata = ''
if(msg == '200'):
    print('got that bish')
    while(msg != 'done'):
        try:
            clientSocket.settimeout(2)
            msg, Serveraddr = clientSocket.recvfrom(2048)
            msg = msg.decode('utf-8')
            filedata = filedata + msg          
        except socket.timeout:
            print('hitty witty')
            break #might lose data? but need in case we miss done

    
    parsedData = handledata(filedata)
    print(parsedData)
    print('broke out the gulag')

    for curFile in parsedData:
        clientSocket.sendto(curFile.encode('utf-8'), Serveraddr)
        accumulatedData = ''
        while(msg != 'done'):
            try:
                msg, Serveraddr = clientSocket.recvfrom(2048)
                accumulatedData = accumulatedData + msg
            except socket.timeout:
                print('u r a failure')
                break
        file = open(curFile, "wb")
        file.write(accumulatedData)
        print('-------------')
        print(file)  
    clientSocket.sendto('done'.encode('utf-8'), Serveraddr)
    input('enter to close')
elif(msg == '404'):
    print('did not find that')
    input('enter to close')
    sys.exit()


    # curFile = parsedData[0]
    # clientSocket.settimeout(None)
    # print('i am sending', curFile)
    # clientSocket.sendto(curFile.encode('utf-8'), Serveraddr)
    # msg, Serveraddr = clientSocket.recvfrom(2048)
    # msg = msg.decode('utf-8')
    # print(msg)
    # file = open(curFile,"wb")
    # file.write(msg)
    # print('-------------')
    # print(file)          

    # for curFile in parsedData:
    #     clientSocket.sendto(curFile.encode('utf-8'), Serveraddr)
    #     try:
    #         msg, Serveraddr = clientSocket.recvfrom(2048)
    #         msg = msg.decode('utf-8')
    #         print(msg)
    #         file = open(curFile,"wb")
    #         file.write(msg)
    #         print('-------------')
    #         print(file)          
    #     except socket.timeout:
    #         print('hitty witty')
    #         break #might lose data? but need in case we miss done
        

 