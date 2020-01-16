import socket
import os

UDP_IP = "127.0.0.1"
UDP_PORT = 10001
SN = os.environ["COMPUTERNAME"]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MESSAGE = str.encode(SN)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
