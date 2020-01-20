import socket
import time

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('www.google.com', 80))
# request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
# sock.send(request.encode('utf-8'))
# response = sock.recv(4096)
# sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("smtp.gmail.com", 587))
sock.send(b"EHLO google.com\n")
time.sleep(1)
resp_smtp = sock.recv(4096)
print(resp_smtp.decode("utf-8"))
sock.close()

# with open("google.txt", "wb") as file:
#     file.write(response)
#     file.write("\n+++SMTP+++\n".encode("utf-8"))
#     file.write(resp_smtp)
