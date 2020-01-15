import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('www.google.com', 80))
content_items = ['GET', '\n']

content = '\n'.join(content_items)

sock.send(content.encode())
result = sock.recv(10024)

my_file = open('google_respond.txt', 'w')

my_file.write(result.decode())

my_file.close()

