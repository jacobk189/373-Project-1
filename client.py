from socket import * #include Python's socket library
import sys

if len(sys.argv) != 4:
    print('not enough arguments')

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
fileName = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_DGRAM)