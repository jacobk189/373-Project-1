from socket import * #include Python's socket library
import sys
from html.parser import HTMLParser

defaultFile = 'index.html'
defaultPort = 3905
defaultName = 'compsci04.snc.edu'

def handledata(filedata):
    parser = HTMLParser()
    parser.feed(filedata)
    parser.handle_starttag('a', [('href')])
    print(parser.get_starttag_text())

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
        #print(msg)
        filedata = filedata + msg
    #parse(filedata)
    handledata(filedata)
    input('enter to close')
    #clientSocket.recvfrom(2048)
elif(msg == '404'):
    print('did not find that hoe')
    input('enter to close')
    sys.exit()