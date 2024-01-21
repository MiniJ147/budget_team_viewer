import socket

#inilizes socket
sock = socket.socket()

PORT = 8080

def startup():
    #starts server on 127.0.0.1:5000
    sock.bind(('127.0.0.1',PORT))

    #listens for 5 connections
    sock.listen(5)

    run()

def run():
    while 1:
        connection, address = sock.accept() #accepts incoming connection

        print("\n[Recieved Connection] ",address)

        #recieving request
        request = connection.recv(1024) #receives 1024 bytes
        msg = request.decode('utf-8')
        print(msg)

        response = "You are connected!\n".encode('utf-8')
        connection.send(response)
        connection.close()

if __name__ == "__main__":
    print("Hello From Server")

    startup()