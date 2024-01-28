from .log import LOG

DEBUG_FLAG = 0

STATUS_SUCCESS = 200
STATUS_FAILURE = 400

def tcp_send_str(sock, msg):
    if DEBUG_FLAG: LOG("DEBUG: SENT")

    sock.send(msg.encode("utf-8"))

def tcp_send(sock, bytes):
    if DEBUG_FLAG: LOG("DEBUG: SEND")

    sock.send(bytes)

def tcp_recv_str(sock) -> str:
    if DEBUG_FLAG: LOG("DEBUG: RECV")

    msg = sock.recv(1024).decode("utf-8")
    return msg

def tcp_recv(sock):
    if DEBUG_FLAG: LOG("DEBUG: Recv")

    return sock.recv(1024)

def tcp_status_send(sock, code):
    if code == STATUS_SUCCESS:
        tcp_send_str(sock,"RESULT: SUCCESS")
    elif code == STATUS_FAILURE:
        tcp_send_str(sock,"RESULT: FAILURE")

