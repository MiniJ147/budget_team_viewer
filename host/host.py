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
    
    #recive ips
    server_ips = tcp_recv_str(con)
    tcp_status_send(con, STATUS_SUCCESS)
    
    print(server_ips)

    #closes the connection
    con.close()

if __name__ == "__main__":
    print(IMPORTANT_MESSAGE)
    startup()

