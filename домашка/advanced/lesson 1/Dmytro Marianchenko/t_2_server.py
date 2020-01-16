import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 10001))

while True:
    data, addr = sock.recvfrom(1024)
    data = bytes.decode(data)
    print(f"{data} connected to the server...")
