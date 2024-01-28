import socket
import sys

sys.path.append('../')

from utils.tcp import *

ip = "127.0.0.1"
port = 8080

IMPORTANT_MESSAGE = '''
===========BTV - Host===========
Information:
 -version: 0.04v

About:
 Used to request commands from
 the server to control 
 clients computers.

================================
'''

def startup():
    # creates a new socket
    con = socket.socket()
    
    # connects to the server
    con.connect((ip, port))
    
    # recives and prints a message from the server
    data = tcp_recv(con)
    num_connections = int.from_bytes(data, "big")
    print("Number of connections: " + str(num_connections))

    #send status
    tcp_status_send(con, STATUS_SUCCESS)

    #recive ips
    server_ips = tcp_recv_str(con)
    tcp_status_send(con, STATUS_SUCCESS)
    
    print(server_ips)

    #closes the connection
    con.close()

if __name__ == "__main__":
    print(IMPORTANT_MESSAGE)
    startup()

