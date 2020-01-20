import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 20000))


sock.send(b'Test message from client')
result = sock.recv(64)
print('Response:', result)


sock.send(b'Test message 2 from client')
result = sock.recv(64)
print('Response:', result)

sock.close()