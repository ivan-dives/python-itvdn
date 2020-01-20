#!/usr/bin/python3
# -*- coding: utf-8 -*_

# Создайте UNIX сокет, который принимает сообщение с двумя числами, разделенными запятой.
# Сервер должен конвертировать строковое сообщения в два числа и вычислять его сумму. После
# успешного вычисления возвращать ответ клиенту.

import socket

# unix_sock = "unix_sock"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('127.0.0.1', 10001))

while True:

    try:
        result, address = sock.recvfrom(4096)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        a, b = map(int, result.decode("utf-8").split(","))
        sum = a + b
        print(sum)

    if result:
        print(type(address))
        print(address)
        data = str(sum)
        sent = sock.sendto(data.encode("utf-8"), address)



