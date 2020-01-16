# Задание 3
# Открыть клиентский TCP сокет на google.com (порт 80),
# сказать в сокет "GET", получить ответ, сохранить в файл

import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('google.com', 80))
    sock.send(b'GET')
    respb = sock.recv(1500)
    with open('google80resp.txt', 'wt') as respfile:
        print(respb.decode('utf-8'), file=respfile)


if __name__ == '__main__':
    main()

