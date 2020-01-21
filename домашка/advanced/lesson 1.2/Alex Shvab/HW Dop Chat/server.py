import socket
import select


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5050))
sock.listen(10)

list_clients = [sock]
print('Start Server')

while True:
    r, w, e = select.select(list_clients, [], [], 1)
    for s in r:
        if s is list_clients:
            user_sock, addr = sock.accept()
            print(addr[0], addr[1])
            list_clients.append(addr)
        else:
            msg = sock.recv(5000)
            for clients in list_clients:
                if (clients is sock) or (clients is s):
                    continue
                clients.send(msg)
