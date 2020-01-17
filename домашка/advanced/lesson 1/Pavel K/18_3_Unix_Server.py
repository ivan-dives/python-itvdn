import socket

sock =socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) 
result = sock.recv(1024)
print('OUT PUT: ', result)
sock.close()

