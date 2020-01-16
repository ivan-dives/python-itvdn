# 1) откройте клиентский TCP сокет на smtp.gmail.com порт 587
# 2) поздоровайтесь с гуглом, скажите "EHLO google.com" (здесь не опечатка, именно EHLO)
# 3) ответ получите и выведите на экран
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('smtp.gmail.com', 587))
hello = 'EHLO google.com'
hello = hello.encode()
s.send(hello)
res = s.recv(10000)
print(res)
s.close()
