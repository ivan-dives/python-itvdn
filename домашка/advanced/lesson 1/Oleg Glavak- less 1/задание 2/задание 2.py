import socket

text = input('Enter message: ')

x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
x.sendto(text.encode('utf-8'), ('127.0.0.1', 15000))
x.close()
