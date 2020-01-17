import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(b"massage from client 2", ( "127.0.0.1", 10001))