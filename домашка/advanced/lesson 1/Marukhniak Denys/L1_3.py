# по третьему заданию - открыть клиентский TCP сокет на google.com (порт 80), сказать в сокет "GET", получить ответ,
# сохранить в файл
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('google.com', 80))
s.send(b'GET / HTTP/1.1\nHost: www.google.com\n\n')  # s.send(b'GET\n')
res = s.recv(730)

with open('get_google.txt', 'wb') as file:
    file.write(res)

s.close()

