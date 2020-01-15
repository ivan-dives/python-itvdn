from socket import *
import sys

host = '127.0.0.1'
port = 10000
addr = (host, port)

udp_socket = socket(AF_INET, SOCK_DGRAM)

data = input('write ident number: ')
if not data:
    udp_socket.close()
    sys.exit(1)


data = str.encode(data)
udp_socket.sendto(data, addr)
data = bytes.decode(data)
data = udp_socket.recvfrom(1024)
print(data)


udp_socket.close()
