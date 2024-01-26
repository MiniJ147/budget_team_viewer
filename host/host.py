import socket

ip = "127.0.0.1"
port = 5050

def startup():
    # creates a new socket
    client = socket.socket()
    
    # connects to the server
    client.connect((ip, port))
    
    # sends a messgae to the server
    message = "Hello.".encode("utf-8")
    client.send(message)
    
    # recives and prints a message from the server
    data = client.recv(1024)
    response = int.from_bytes(data, "big")
    print("Number of connections: " + str(response))
    
    #recieves and prints the ip addresses of the connections from the server
    response2 = client.recv(1024)
    print("Current connections:\n" + response2.decode("utf-8"))

    #closes the connection
    client.close()

if __name__ == "__main__":
    startup()

