#!/usr/bin/python
import socket
from crypto import Random

if __name__ == '__main__':
    host = ''
    port = 8080
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((host, port))
    socket.listen(1)
    while True:
        clientSocket, addr = socket.accept()
        print("Connection from " + repr(addr) + " url: " + str(clientSocket.recv(1024)).split(" ")[1])
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
