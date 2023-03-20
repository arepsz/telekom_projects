import sys
from sys import argv
import struct

firstPacker = struct.Struct('9sif')
secondPacker = struct.Struct('f?c')
thirdPacker = struct.Struct('ci9s')
fourthPacker = struct.Struct('f9s?')

firstFile = argv[1]
secondFile = argv[2]
thirdFile = argv[3]
fourthFile = argv[4]

with open(firstFile, 'rb') as f:
    data1 = f.read(struct.calcsize('9sif'))
    print(firstPacker.unpack(data1))

with open(secondFile, 'rb') as f:
    data2 = f.read(struct.calcsize('f?c'))
    print(secondPacker.unpack(data2))

with open(thirdFile, 'rb') as f:
    data3 = f.read(struct.calcsize('ci9s'))
    print(thirdPacker.unpack(data3))

with open(fourthFile, 'rb') as f:
    data4 = f.read(struct.calcsize('f9s?'))
    print(fourthPacker.unpack(data4))


packer1 = struct.Struct('12si?')
packer2 = struct.Struct('f?c')
packer3 = struct.Struct('i10sf')
packer4 = struct.Struct('ci13s')

values1 = (b"elso", 70, True)
packed_date1 = packer1.pack(*values1)
print(packed_date1)

values2 = (73.5, False, b'X')
packed_date2 = packer2.pack(*values2)
print(packed_date2)

values3 = (61, b"masodik", 80.9)
packed_date3 = packer3.pack(*values3)
print(packed_date3)

values4 = (b'Z', 92, b"harmadik")
packed_date4 = packer4.pack(*values4)
print(packed_date4)



