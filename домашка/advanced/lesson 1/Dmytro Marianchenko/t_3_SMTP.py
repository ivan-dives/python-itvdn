import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("smtp.gmail.com", 587))
sock.send(b"EHLO google.com")
resp = sock.recv(5000)
sock.close()
resp = bytes.decode(resp)
print()
print(resp)
