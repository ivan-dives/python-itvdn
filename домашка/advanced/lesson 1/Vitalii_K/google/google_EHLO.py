import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('smtp.gmail.com', 587))
s.send(b'EHLO google.com')
x = s.recv(1000)
s.close()

print(x)
