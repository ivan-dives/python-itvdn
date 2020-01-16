import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.google.com', 80))
request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
sock.send(request.encode('utf-8'))
response = sock.recv(4096)
sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("smtp.gmail.com", 587))
sock.send("EHLO google.com".encode("utf-8"))
resp_smtp = sock.recv(4096)
sock.close()

with open("google.txt", "wb") as file:
    file.write(response)
    file.write("\n+++SMTP+++\n".encode("utf-8"))
    file.write(resp_smtp)
