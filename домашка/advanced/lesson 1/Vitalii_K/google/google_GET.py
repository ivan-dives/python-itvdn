import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('google.com', 80))
s.send(b'GET\n')
x = s.recv(100000)
s.close()

with open('google_GET.txt', 'wb') as g:
    g.write(x)
