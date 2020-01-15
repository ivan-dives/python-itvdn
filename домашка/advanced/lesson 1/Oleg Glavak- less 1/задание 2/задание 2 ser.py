import socket

x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
x.bind(('127.0.0.1', 15000))
mess = x.recv(1200)
mess = mess.decode('utf-8')
print(mess)
x.close()