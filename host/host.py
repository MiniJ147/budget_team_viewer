import socket

ip = "127.0.0.1"
port = 5050

def startup():
    # creates a new socket
    client = socket.socket()
    
    # connects to the server
    client.connect((ip, port))
    
    # recives and prints a message from the server
    data = client.recv(1024)
    num_connections = int.from_bytes(data, "big")
    print("Number of connections: " + str(num_connections))

    #send status
    client.send("SUCESS".encode("utf-8"))

    #recive ips
    server_ips = client.recv(1024).decode("utf-8")
    client.send("SUCESS".encode("utf-8"))
    
    print(server_ips)

    #closes the connection
    client.close()

if __name__ == "__main__":
    startup()

