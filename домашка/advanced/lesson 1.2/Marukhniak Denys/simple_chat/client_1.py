import socket

name = input('Enter your name in chat: ')

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 10000))
    text = input(f'{name}: ')
    msg = name + ': ' + text
    sock.send(msg.encode())
    result = sock.recv(64)
    print(result.decode())
    sock.close()
