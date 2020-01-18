import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
#sock.bind(('', 8888))
sock.bind('/tmp/mysocket')
result = sock.recv(1024)
print('Message', result.decode('utf-8'))
sock.close()

exit()

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 10000))
s.listen(1)

#time.sleep(30)

client_socket, addr = s.accept()
print(f'accept returned {addr=}')
#time.sleep(30)
msg = client_socket.recv(100)
msg = msg.decode('utf-8')
print(f'received {msg}')
client_socket.close()

s.close()

exit()


# example 3 (TCP server socket)
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print('Message', result.decode('utf-8'))

exit()

import socket

# IPv4 / UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 10000))
msg = s.recv(100)
msg = msg.decode('utf-8')
print(f'received "{msg}"')
s.close()

exit()

# IPv6 / TCP
#s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)




# example 1 (UDP server socket)
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 8888))
result = sock.recv(1024)
print('Message', result.decode('utf-8'))
sock.close()