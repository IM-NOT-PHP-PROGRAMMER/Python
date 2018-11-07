#!/usr/bin/python
import socket

if __name__ == '__main__':
    host = ''
    port = 8080
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((host, port))
    socket.listen(10)
    while True:
        clientSocket, addr = socket.accept()

        clientRequest = str(clientSocket.recv(1024))
        clientPath = clientRequest.split(" ")[1]
        print("Connection from {addr} path: {clientPath}".format(addr=addr, clientPath=clientPath))

        if not "?" in clientPath or clientPath[:clientPath.index("?")] != "/proceed" or not "?e=" in clientPath or "&" in clientPath[(clientPath.index("?") + 3):]:
            clientSocket.close()
            continue

        e = clientPath[(clientPath.index("?") + 3):]

        clientSocket.sendall(bytes("HTTP/1.0 200 OK\n"
                                   "Content-Type: text/html\n"
                                   "Connection: Close\n"
                                   "Access-Control-Allow-Origin: *\r\n"
                                   "\r\n"
                                   "<html>\n"
                                   "<head>\n"
                                   "<title>Success</title>\n"
                                   "</head>\n"
                                   "<body>\n"
                                   "Boo!\n"
                                   "</body>\n"
                                   "</html>\n", "UTF-8"))
        clientSocket.close()
