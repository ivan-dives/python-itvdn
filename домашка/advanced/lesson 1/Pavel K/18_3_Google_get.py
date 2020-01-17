# открыть клиентский TCP сокет на google.com (порт 80), сказать в сокет "GET", получить ответ, сохранить в файл.
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('google.com', 80))
s.send(b'GET\n')
res = s.recv(730)

with open('g1.txt', 'wb') as file:
    file.write(res)

s.close()
