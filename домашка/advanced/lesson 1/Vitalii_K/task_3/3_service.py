import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 11111))
s.listen(1)
cs, a = s.accept()
x_pack = cs.recv(100)
x_unpack = struct.unpack('ii', x_pack)
y = sum(x_unpack)
y_pack = struct.pack('i', y)
cs.send(y_pack)
s.close()
