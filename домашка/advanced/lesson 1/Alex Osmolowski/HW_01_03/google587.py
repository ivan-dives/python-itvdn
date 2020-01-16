# Задание 3
# 1) откройте клиентский TCP сокет на smtp.gmail.com порт 587
# 2) поздоровайтесь с гуглом, скажите "EHLO google.com" (здесь не опечатка, именно EHLO)
# 3) ответ получите и выведите на экран

import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('smtp.gmail.com', 587))
    sock.send(b'EHLO google.com')
    respb = sock.recv(1500)
    print(respb.decode('utf-8'))


if __name__ == '__main__':
    main()