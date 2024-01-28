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

    #send status
    tcp_status_send(con, STATUS_SUCCESS)

    #recive ips
    server_ips = tcp_recv_str(con)

    # prints the number of current connections and the ips of the clients
    string = ""
    ip_list = []
    count = 0
    while server_ips[count] != "X":
        if server_ips[count] == ",":
            ip_list.append(string)
            string = ""
        else:
            string += server_ips[count]
        count += 1
    ip_list.append(string)

    tcp_status_send(con, STATUS_SUCCESS)
    
    print("Number of connections:", end=" ")
    print(len(ip_list))
    print("\n")
    
    print("Connected IP Addresses: ")
    for _ip in ip_list:
        print(_ip + '\n')
        

    #closes the connection
    con.close()

if __name__ == "__main__":
    print(IMPORTANT_MESSAGE)
    startup()

