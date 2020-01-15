import socket
import os
t = os.environ['COMPUTERNAME']  # determine the name of your device
t = str.encode(t) # encoding from str to bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(t, ('127.0.0.1', 9999))
