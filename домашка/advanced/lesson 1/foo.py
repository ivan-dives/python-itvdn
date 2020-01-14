import socket

text = input('траливали ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 10000))
s.send(text.encode('utf-8'))
s.close()

exit()

import socket

#print(type(b'text'))
#exit()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'message', ('127.0.0.1', 10000))
s.close()
exit()

# example 1 (UDP client socket )
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Test message', ('localhost', 8888))