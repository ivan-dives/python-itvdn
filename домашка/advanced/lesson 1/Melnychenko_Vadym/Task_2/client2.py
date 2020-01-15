import socket

n = 0
print(f'To exit, type "off"')
print(f'Enter "close" to exit socket')
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if n == 0:
        s.sendto(b'client_2_online', ('127.0.0.1', 10001))
    n += 1
    message = input(f'message {n}: ')
    data = {'ID': "client_2", 'Message': message}
    data = str(data).encode('utf-8')
    if message == 'close':
        s.sendto(b'close', ('127.0.0.1', 10001))
        break
    elif message == 'off':
        print('Exit to client')
        break
    else:
        s.sendto(data, ('127.0.0.1', 10001))
    s.close()
