import socket

host = 'localhost'
port = 6767

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

print("Server started listening on port :: {}".format(port))

s.listen(1)  # No. of connection going to accept

connection, address = s.accept()

filename = connection.recv(1024)

try:
    f = open(filename, 'rb')
    content = f.read()
    connection.send(content)
    f.close()
except:
    print("file not found")
    connection.send(b"File doesn't exist")

connection.close()