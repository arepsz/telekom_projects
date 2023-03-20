import sys
import socket
import hashlib

server_address = (sys.argv[1], int(sys.argv[2]))
proxy_address = (sys.argv[3], int(sys.argv[4]))

server_connection = socket.socket()
server_connection.connect(server_address)
proxy_connection = socket.socket()
proxy_connection.connect(proxy_address)

file = open(sys.argv[6], 'rb')
data = file.read(1024)
md5 = hashlib.md5()
while data:
    server_connection.send(data)
    md5.update(data)
    data = file.read(1024)
server_connection.close()

msg = ('BE|' + sys.argv[5] + '|60|' + str(len(md5.hexdigest())) + '|' + md5.hexdigest()).encode('utf-8')
proxy_connection.sendall(msg)
data = proxy_connection.recv(1024)
