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

### AFK8S6_barkoba

Let's make a question / answer application. The server should be able to serve several clients. The server should choose an integer between 1..100 at random. Clients try to guess the number.

    The client uses a logarithmic search to find the intended number. The client should NOT work from the standard input.
    If a client has guessed the number, the server sends the message "End" (V) to every new client message, after which the clients exit.
    Upon receiving Win (Y), Lose (K) and End (V) messages, the client disconnects and terminates the connection. In case of Yes (I) / No (N), it continue the questioning.
    Use TCP for communication!
    The server uses SELECT funtion to serve multiple clients!!!!!
    If the game is over, the server send End (V) for every question!

Message format:

    Form Client: bytes format one char, one integer. (struct) Do not use the byte order manipulation operator! ('!')
        The char is: <: lower then, >: bigger then, =: equals
        ex: ('>',10) //the number is bigger then 10
    From Server: same bytes format , but the number is irrelevant (struct)
        The char is: I: Yes, N: No, K: Quit, Y: Win, V: End
        ex: ('V',0)


Parameters of the script:

    python3 client.py < hostname > < port number >
        ex: python3 client.py localhost 10000
    python3 server.py < hostname > < port number >
        ex: python3 server.py localhost 10000

### NetCopy
