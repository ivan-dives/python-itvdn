import socket


service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
service.bind(("127.0.0.1", 10000))
service.listen(1)

client_socket, addr = service.accept()
msg = client_socket.recv(100)
msg = msg.decode("utf-8")
lst = [int(x) for x in msg.split(",")]
res = str(lst[0] + lst[1])
client_socket.send(res.encode())
service.close()
