# 373-Project-1
To run the UDP version of our project you will need to download client.py to your computer and server.py to compsci04. Once you have the applications in the right place you will need to ensure that 
the index.html file and the index_files folder with the various images are stored in the same folder as the server.py application. Further, ensure that there is an empty folder in the same folder as
client.py also called index_files which will fill up with the recieved images. When all the folders and files are in the correct locations simply run the server.py on compsci04 using the command
" python3 server.py " and the client.py from the command line using the command " py client.py "

To run the TCP version of our project you will first need to choose if you will be testing locally or remotly. If you are testing locally you will need to download TCPclient.py and TCPserver.py to
your computer along with the index.html and index_files. With all of these installed you will now need to create a new folder called server_files and store the index_files folder inside this folder.
Next create an empty index_files outside of the server_files folder. This second index_files will be used to store the recieved files while the server_files are the original source files. Next you
will need to execute TCPserver.py in the command line and then TCPclient.py. If you choose to test remotly you will need to download TCPclient.py to your computer and create the empty index_files folder
in the same location. You will also need to download TCPserver.py, index.html, and index_files to compsci04. You will then need to alter TCPserver.py to no longer use the server_files route to open
the index files. To do this simply comment out the lines which alter the path and un-comment the line which says "for testing on compsci04." After altering TCPserver.py you will also need to alter
TCPclient.py. In TCPclient.py change the ServerName variable to "compsci04.snc.edu" instead of "127.0.0.1" Now you should be able to execute the TCPserver.py with " python3 TCPserver.py " on compsci04
and TCPclient.py with " py TCPclient.py " on your local terminal. 

*Note: We have not tested on compsci04 for TCP as we were under the impression that the ports were closed but following the instructions should work in theory

*Note: Code is written to handle command line variable inputs however the provided files (index.html and associated images) are used as the defaults if testing with others variables must be provided