import socket


request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.com", 80))
s.send(request)
result = s.recv(10000)

with open("google_get.txt", "wb") as file:
    file.write(result)

s.close()

request = b"EHLO google.com"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("smtp.gmail.com", 587))
s.send(request)
result = s.recv(10000)
print(result)