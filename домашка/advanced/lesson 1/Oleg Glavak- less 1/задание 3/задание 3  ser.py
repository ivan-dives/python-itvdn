import socket

r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.bind(('127.0.0.1', 10000))
r.listen(1)

client_socket, addr = r.accept()
mess = client_socket.recv(12000)
mess = mess.decode('utf-8')
print(mess)

client_socket.close()
r.close()