import socket

ip = "127.0.0.1"
port = 8080

def startup():
    # creates a new socket
    client = socket.socket()
    
    # connects to the server
    client.connect((ip, port))
    
    # sends a messgae to the server
    message = "Hello.".encode("utf-8")
    client.send(message)
    
    # recivees and prints a message from the server
    response = client.recv(1024)
    print(response.decode("utf-8"))
    
    #closes the connection
    client.close()

if __name__ == "__main__":
    startup()

