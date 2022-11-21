import socket

#Define the IP, Port, and Recived data variables
IP = "127.0.0.1"
PORT = 1234
RCV_DATA = ""

#Set up the sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))

#Listen for connections
while(1):
    server_socket.listen(1)
    server_conn, addr = server_socket.accept()
    print ('Connected by', addr)
    #Recive data and reply with an echo.
    while 1:
        RCV_DATA = server_conn.recv(1024)
        if not RCV_DATA: break
        print (f"The server received this data: {RCV_DATA}")
        server_conn.sendall(RCV_DATA)
