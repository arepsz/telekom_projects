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

### netcopy

Create a netcopy client/server application that enables the transfer of a file and the verification of the transferred data using a CRC or MD5 checksum! During the task, threecomponents/programs must be prepared:

1. Checksum server: Store data: (file identifier, checksum length, checksum, expiration (in seconds)). Details of the protocol can be found below.
2. Netcopy client: transfers a file contained in a command line argument to the server. During/at the end of the transfer, it calculates a checksum for the file and then uploads it together with the file ID to the Checksum server. The expiration time is 60 seconds. The file identifier is an integer, which is also must be specified in a command line argument.
3. Netcopy server: Waits for a client to connect. After connecting, it receives the transferred bytes and places them in the file in the command line argument. At the end, it retrieves the checksum associated with the file identifier from the Checksum server and checks the correctness of the transferred file, as a result of which it is also written to standard output. The file identifier must also be a command line argument here.
Checksum server

    Insert message
        Format: text
        Structure: BE|< file id >|< validity in seconds >|< checksum length in bytes >|< checksum bytes >
        The "|" is the delimiter character
        Example: BE|1237671|60|12|abcdefabcdef
            In this case: the file number: 1237671, the validity period is 60 seconds, the checksum is 12 bytes, the checksum itself is abcdefabcdef
            Response message: OK
    Take out message
        Format: text
        Structure: KI|< file id >
        The "|" is the delimiter character
        Example: KI|1237671
            That is, we are asking for the checksum for file ID 1237671
            Response message: < checksum length in bytes >| < checksum bytes >
            Example: 12|abcdefabcdef
        If there is no checksum, it sends: 0|
    Run
        python3 checksum_srv.py < ip > < port >
            < ip > - e.g. localhost is the address of the server when binding
            < port > - will be available on this port
        The server runs in an endless cycle and can serve several clients at the same time. The communication is TCP, it only handles the above messages.
        Post-expiration checksums are deleted, but it is enough if you only check them at the next request.

NetCopy Client

    Operation:
        Connects to the server, whose address and port you receive in command line arguments.
        Sequential transfer of file bytes to the server.
        It communicates with the Checksum server as described there.
        After transferring the file and placing the checksum, disconnect and terminal.
    Run:
        python3 netcopy_cli.py < srv_ip > < srv_port > < chsum_srv_ip > < chsum_srv_port > < file id > < filename with path >
        < file id >: integer
        < srv_ip > < srv_port >: netcopy server address
        < chsum_srv_ip > < chsum_srv_port >: Checksum server address

NetCopy Server

    Operation:
        Binds the socket to the address specified in the command line argument.
        Waiting for a client.
        If accepted, it accepts the bytes of the file sequentially and writes them to the file specified in the paragraph line argument.
        When an end-of-file signal is read, it closes the connection and then checks the file with the Checksum server.
        It communicates with the Checksum server as described there.
        In the event of an error, the following should be written to stdout: CSUM CORRUPTED
        If the transfer is correct, the following should be written to stdout: CSUM OK
        After receiving and checking the file, the program is terminal.
    Run:
        python3 netcopy_srv.py < srv_ip > < srv_port > < chsum_srv_ip > < chsum_srv_port > < file id > < filename with path >
            < file id >: integer same as for the client - based on this, it requests the checksum from the server
            < srv_ip > < srv_port >: address of the netcopy server - required when binding
            < chsum_srv_ip > < chsum_srv_port >: Checksum server address
            < file name > : write the received bytes here
