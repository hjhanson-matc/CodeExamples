import socket

#Define the IP and PORT to send to
IP = "127.0.0.1"
PORT = 1234

#Set up the sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

#A while connected loop
while 1:
    #Have the user type a message to the server
    SND_DATA = input("Chat (type quit to end) ->")
    #Check if the message is quit, if not, send to server and recive reply
    if SND_DATA != 'quit':
        SND_DATA = SND_DATA.encode("utf-8")
        client_socket.send(SND_DATA)
        RCV_DATA = client_socket.recv(1024)
        print (RCV_DATA)
    #If the message is quit, end the connection and close the script
    elif SND_DATA == 'quit':
        client_socket.close()
        break
