#!/usr/bin/python
import socket

if __name__ == '__main__':
    host = ''
    port = 8080
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((host, port))
    socket.listen(1)
    while True:
        clientSocket, addr = socket.accept()
        print("Connection from " + repr(addr))
        clientSocket.sendall(bytes("""HTTP/1.0 200 OK
Content-Type: text/html
Connection: Close

<html>
<head>
<title>Success</title>
</head>
<body>
Boo!
</body>
</html>
""", "UTF-8"))
        clientSocket.close()
