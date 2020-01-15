import socket

n = 0

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 10001))
    msg = s.recv(1024)
    msg = msg.decode('utf-8')
    if n == 0:
        print(f'{msg}')
    elif n > 0:
        print(f'Message {n}: {msg}')
    n += 1
    if msg == "close":
        print('Close socket')
        s.close()
        break
