import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('smtp.gmail.com', 587))
content_items = ['EHLO google.com', '\n']

content = '\n'.join(content_items)

print('--- HTTP MESSAGE ---')
print(content)
print('--- END OF MESSAGE ---')

sock.send(content.encode())
result = sock.recv(10024)

print(result.decode())
