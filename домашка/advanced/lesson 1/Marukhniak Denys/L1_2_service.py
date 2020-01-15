import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 10000))
msg = s.recv(100)
msg = msg.decode('utf-8')
print(f'Name of device: "{msg}"')
s.close()
