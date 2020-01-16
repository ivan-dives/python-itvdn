import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('smtp.gmail.com', 587))
sock.send(b'EHLO google.com')

mass = sock.recv(1500)
print('Message', bytes.decode(mass))
sock.close()

