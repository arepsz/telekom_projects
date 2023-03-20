import sys
from datetime import datetime, timedelta
import socket
import select
import struct

host = sys.argv[1]
ip = int(sys.argv[2])

server_address = (host, ip)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(server_address)
server.listen(5)

inputs = [server]
md5_save = {}

while inputs:
	timeout = 1
	readable,writeable,exceptable = select.select(inputs,[],inputs,timeout)

	if not (readable or writeable or exceptable):
		continue

	for s in readable:
		if s is server:
			client, client_addr = s.accept()
			client.setblocking(1)
			inputs.append(client)
		else:
			data = s.recv(1024)
			if data:
				msg = str(data, 'utf-8').split('|')
				request_type = msg[0]
				fileID = msg[1]
				if request_type == 'BE':
					checksum_length = int(msg[2])
					md5_length = int(msg[3])
					md5_value = msg[4]
					md5_save[fileID] = {'length': md5_length, 'value': md5_value, 'checksum_length': checksum_length, 'timestamp': datetime.now()}
					s.send(b'OK')

				elif request_type == 'KI':
					md5 = md5_save.get(fileID)
					if md5:
						if datetime.now() - md5['timestamp'] < timedelta(seconds=md5['checksum_length']):
							msg = str(md5['length']) + '|' + md5['value']
						else:
							msg = '0|'
					else:
						msg = '0|'
					s.sendall(msg.encode('utf-8'))
				else:
					print('Invalid request')
			else:
				inputs.remove(s)
				s.close()

	for s in exceptable:
		inputs.remove(sock)
		s.close()
