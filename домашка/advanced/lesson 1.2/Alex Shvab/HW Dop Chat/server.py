import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5050))
list_clients = []
print('Start Server')
while 1:
    data, addr = sock.recvfrom(1024)
    print(addr[0], addr[1])
    if addr not in list_clients:
        list_clients.append(addr)
    for clients in list_clients:
        if clients == addr:
            continue
        sock.sendto(data, clients)
