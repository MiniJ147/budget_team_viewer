import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 8080

    client = socket.socket()
    client.connect((ip, port))
    message = "Hello.".encode("utf-8")
    client.send(message)
    response = client.recv(1024)
    print(response.decode("utf-8"))
    client.close()

