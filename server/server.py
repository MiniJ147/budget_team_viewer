import socket
import sys
sys.path.append('../')

from utils.tcp import *
from utils.log import *

#inilizes socket
sock = socket.socket()

PORT = 8080

EXAMPLE_DATA = ['68.129.180.01','28.400.180.01','70.129.120.01']

IMPORTANT_MESSAGE = '''
==========BTV - Server==========
Information:
 -version: 0.04v

About:
 Used as the middleman to handle
 request between host and clients

================================
'''

def startup():
    #starts server on 127.0.0.1:5000
    sock.bind(('127.0.0.1',PORT))

    #listens for 5 connections
    sock.listen(5)

    run()

def run():
    while 1:
        con, address = sock.accept() #accepts incoming connection

        print("\n[Recieved Connection] ",address)

        '''make it so we send in one network request instead of muitple. One big str'''
        #loops through every ip in connected and sends to the host
        ip_list_str = ""
        for ip in EXAMPLE_DATA:
            ip_list_str += ip + '\n,'
        
        #parses out last ,
        ip_list_str = ip_list_str[:-1]
        ip_list_str += 'X' #add escape char 

        #sending one big string and recieving result message
        tcp_send_str(con,ip_list_str)
        
        print(tcp_recv_str(con))
        
        con.close()

if __name__ == "__main__":
    print(IMPORTANT_MESSAGE)
    startup()