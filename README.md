# telekom_projects
All projects for the telecommunication networks subject at ELTE-IK.

Folders:
### Client
Circuit simulation

Write a program which simulates the allocation and deallocation of resources according to the topology, capacities and demands outlined in the given JSON file!

JSON file for testing: cs1.json

Parameters of the script: python3 client.py cs.json

Structure of the output:

     event number. < event name >: < node1 > <-> < node2 > st:< simulation time > [- < successful/unsuccessful >] 


Ex.:

1. demand allocation: A<->C st:1 – successful
2. demand allocation: B<->C st:2 – successful
3. demand deallocation: A<->C st:5
4. demand allocation: D<->C st:6 – successful
5. demand allocation: A<->C st:7 – unsuccessful
…

### Client(1)
Parameters of the script:

    python3 client.py < file1 > < file2 > < fil3 > < fil4 >
        pl: python3 client.py db1.bin db2.bin db3.bin db4.bin

Example output:
(b'F', b'123456789', 35)
(35, 37.29999923706055, True)
(True, b'123456789', b'F')
(35, b'F', 37.29999923706055)
b'elso\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00S\x00\x00\x00\x01'
b'\x00\x00\xadB\x00X'
b'J\x00\x00\x00masodik\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xcc\xbbB'
b'Z\x00\x00\x00i\x00\x00\x00harmadik\x00\x00\x00\x00\x00\x00\x00\x00'
