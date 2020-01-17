import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("smtp.gmail.com", 587))
resp = sock.recv(1024)
print(resp)
sock.send(b"EHLO google.com\n")
resp = sock.recv(1024)
print()
print(resp)
sock.close()
resp = bytes.decode(resp)
