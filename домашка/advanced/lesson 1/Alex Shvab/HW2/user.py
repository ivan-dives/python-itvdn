import socket


user = socket.gethostname()
user = user.encode("utf-8")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(user, ("127.0.0.1", 10000))
s.close()
