import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('smtp.gmail.com', 587))
text = 'EHLO google.com'
text = str.encode(text)
sock.send(text)
result = sock.recv(512)
print('OUT PUT: ', result)
sock.close()
