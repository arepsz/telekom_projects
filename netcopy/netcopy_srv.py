import sys
import socket
import hashlib

server_address = (sys.argv[1], int(sys.argv[2]))

server = socket.socket()
server.bind(server_address)
server.listen(5)

proxy_connection = socket.socket()
proxy_connection.connect((sys.argv[3], int(sys.argv[4])))

connection, address = server.accept()

file = open(sys.argv[6], 'wb')

data = connection.recv(1024)
md5 = hashlib.md5()
while data:
	file.write(data)
	md5.update(data)
	data = connection.recv(1024)
connection.close()

fileID = 'KI|' + sys.argv[5]
proxy_connection.sendall(fileID.encode('utf-8'))
data = proxy_connection.recv(1024)

msg = data.decode('utf-8').split('|')
if int(msg[0]) == 0 or int(msg[0]) != len(md5.hexdigest()) or msg[1] != md5.hexdigest():
	print('CSUM CORRUPTED')
else:
	print('CSUM OK')
