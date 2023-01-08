from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerSock.bind(("", 8888))
tcpSerSock.listen(10)
# Fill in end.

while 1:
    # Start receiving data from the client
    print('\nReady to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print("Received a connection from:", addr)
    flag = False
    message = tcpCliSock.recv(4096)
    print('message received is')

    if message.split()[1] is None:
        continue

    print(message)

    # Extract the filename from the given message
    file = message.split()[1]
    filename = file.split('/')[1]  # .partition("/")[2]
    # to read for blocked urls
    file2 = message.split()[1].partition("/")[2]

    URLf = open("URL-block.txt", "r")

    for line in URLf.readlines():
        line = line.split('\n')[0]
        if line == file2:
            print("This URL is blocked")
            flag = True
        else:
            fileExist = "false"
            filetouse = file
            print("file to use is: ", filetouse)

    if not flag:
        try:
            # Check wether the file exist in the cache
            f = open(filetouse[1:], "rb")  # [1:]
            outputdata = f.read()
            fileExist = "true"
            # ProxyServer finds a cache hit and generates a response message
            tcpCliSock.sendall("HTTP/1.0 200 OK\r\n")
            tcpCliSock.sendall("Content-Type:text/html\r\n")  # mod
            tcpCliSock.sendall("Content-Type: image/jpeg\r\n")
            # tcpCliSock.send("\r\n")
            # Fill in start.
            for i in range(0, len(outputdata)):
                tcpCliSock.send(outputdata[i])
            print('Read from cache')
            # Fill in end.

        # Error handling for file not found in cache
        except IOError:
            if fileExist == "false":
                # Create a socket on the proxy server
                file = file[1:]
                hostn = file
                c = socket(AF_INET, SOCK_STREAM)
                hostn = file.replace("www.", "", 1)
                print(hostn)
                try:
                    print('connected to port 80')
                    # Create a temporary file on this socket and ask port 80 for the file requested by the client
                    fileobj = c.makefile('rwb', 0)
                    print(hostn)
                    if not "Referer" in message:
                        print("**************Connecting to server***********")
                        # Connect to the socket to port 80
                        c.connect((hostn, 80))
                        con = filename
                        fileobj.write(b'GET / HTTP/1.0\r\n\r\n')
                    else:
                        print("**************Get path in referer: " + hostn)
                        c.connect((con, 80))
                        fileobj.write(b'GET /' + hostn + 'HTTP/1.0\r\n\r\n')

                    buffer = fileobj.read()
                    # recv = c.recv(15000000)
                    tmpFile = open("./" + filename, "wb+")
                    tcpCliSock.send("HTTP/1.0 200 OK\r\n")
                    for i in range(0, len(buffer)):
                        tmpFile.write(buffer[i])
                        tcpCliSock.sendall(buffer[i])
                    # tmpFile.write(recv)
                    print('cache saved')

                except:
                    print("Illegal request")

            else:
                # HTTP response message for file not found
                # Fill in start.
                errorSend = open("404Error.txt")
                tcpCliSock.send("HTTP/1.0 404 Error \r\n")
                tcpCliSock.send("Content-Type:text/html\r\n")
                tcpCliSock.send(errorSend.read())
                # Fill in end.
        # Close the client and the server sockets
        tcpCliSock.close()
# Fill in start.
tcpSerSock.close()
# Fill in end.
