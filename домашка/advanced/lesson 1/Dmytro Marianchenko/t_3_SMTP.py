import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("smtp.gmail.com", 587))
resp = sock.recv(1024)
print()
print(resp.decode("utf-8"))
sock.send(b"EHLO google.com\n")
resp = sock.recv(1024)
print()
print(resp.decode("utf-8"))
sock.close()