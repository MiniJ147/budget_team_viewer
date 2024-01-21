import socket

#inilizes socket
sock = socket.socket()

PORT = 8080

EXAMPLE_DATA = ['68.129.180.01','28.400.180.01','70.129.120.01']

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

        #send the size of current connections
        number_of_connections = len(EXAMPLE_DATA)
        connection.send(number_of_connections.to_bytes(2,"big")) #sending int as bytes

        #loops through every ip in connected and sends to the host
        for ip in EXAMPLE_DATA:
            connection.send(ip.encode('utf-8'))

        connection.close()

if __name__ == "__main__":
    print("Hello From Server")

    startup()