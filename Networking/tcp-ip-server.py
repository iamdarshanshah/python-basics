import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

print("Server started listening on port :: {}".format(port))

s.listen(1)  # No. of connection going to accept

connection, address = s.accept()

print('Connection from {}'.format(str(address)))

connection.send(b"Hello, how are you")
connection.send("Bye".encode())

connection.close()