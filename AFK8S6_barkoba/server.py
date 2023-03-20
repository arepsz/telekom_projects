import socket
import select
import sys
import struct
from random import randint

host = sys.argv[1]
ip = int(sys.argv[2])

server_address = (host, ip)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.settimeout(1.0)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server.bind(server_address)

server.listen(5)

inputs = [server]

win = False
packer = struct.Struct('ci')
guess = randint(1, 100)
print("Gondoltam egy számra: " + str(guess))


while inputs:
	timeout = 1
	readable,writeable,exceptable = select.select(inputs,inputs,inputs,timeout)

	if not (readable or writeable or exceptable):
		continue

	for s in readable:
		try:
			if s is server:
				client, client_addr = s.accept()
				client.setblocking(1)
				inputs.append(client)
			else:
				data = s.recv(200)
				if data:
					if win:
						valasz = ('V'.encode(), int(0))
						s.send(packer.pack(*valasz))
						inputs.remove(s)
						s.close()

					else:
						unpacked_data = packer.unpack(data)
						operator = unpacked_data[0].decode('utf-8')
						num = unpacked_data[1]
						valasz = ''
						if operator == '>':
							if guess > num:
								valasz = 'I'
							else:
								valasz = 'N'
						elif operator == '<':
							if guess < num:
								valasz = 'I'
							else:
								valasz = 'N'
						elif operator == '=':
							if guess == num:
								valasz = 'Y'
							else:
								valasz = 'K'
						packed_response = packer.pack(valasz.encode('utf-8'), 0)
						s.sendall(packed_response)
						if valasz == 'Y':
							print(str(s.getpeername()) + " nyert!")
							print(str(s.getpeername()) + " kilépett!")
							inputs.remove(s)
							s.close()
							win = True

		except socket.error as m:
			print(f"Hiba, a {str(s.getpeername())} játékost kilépteti a szerver!")
			inputs.remove(s)
			s.close()
	if len(inputs) == 1:
		guess = randint(1, 100)
		print("Vége a játéknak\n")
		print("Új számra gondoltam: " + str(guess))
		win = False
