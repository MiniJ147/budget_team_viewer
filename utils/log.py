from datetime import datetime

def LOG(msg):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("[LOG]: "+str(current_time)+" | "+str(msg))