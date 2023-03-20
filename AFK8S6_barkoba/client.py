import socket
import sys
import time
import select
import struct
import random

host = sys.argv[1]
ip = int(sys.argv[2])
server_address = (host, ip)

packer = struct.Struct('ci')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(server_address)
client.settimeout(1.0)

low = 1
high = 100
kozep = 0
flip = random.getrandbits(1)
ended = False

while not ended:
    try:
        if (low < high):
            kozep = int((low + high) / 2)
            if flip:
                tipp = ('>', kozep)
            else:
                tipp = ('<', kozep)
        else:
            tipp = ('=', low)
        values = tipp[0].encode('utf-8'), tipp[1]
        print("Guess: x{}{}".format(tipp[0], kozep))
        packed_request = packer.pack(*values)
        client.sendall(packed_request)
    except socket.timeout:
        pass
    except socket.error as e:
        print(e)
        break

    try:
        data = client.recv(200)
        if not data:
            print("Server down")
            sys.exit()
        else:
            print(packer.unpack(data))
            unpacked_data = packer.unpack(data)
            valasz = unpacked_data[0].decode('utf-8')
            if valasz == 'I':
                if flip:
                    low = kozep + 1
                else:
                    high = kozep - 1
            elif valasz == 'N':
                if flip:
                    high = kozep
                else:
                    low = kozep
            elif valasz == 'Y':
                print("Nyertem! :)")
                ended = True
            elif valasz == 'K':
                print("Vesztettem! :(")
                ended = True
            elif valasz == 'V':
                print("Más nyerte a játékot! :(")
                ended = True
            flip = not flip
    except SystemExit as m:
        client.close()
        break
    except socket.timeout:
        pass
    except socket.error as e:
        print("hiba",e)
        break

    try:
        time.sleep(random.randint(1, 5))
    except KeyboardInterrupt:
        print("\nKilépés")
        sys.exit()
