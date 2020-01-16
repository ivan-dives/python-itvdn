import socket
import os

SN = os.environ["COMPUTERNAME"]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MESSAGE = str.encode(SN)
sock.sendto(MESSAGE, ("127.0.0.1", 10001))
