import socket


service = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
service.bind(("127.0.0.1", 10000))
msg = service.recv(100)
msg = msg.decode("utf-8")
print(f"User {msg} connected")
service.close()
