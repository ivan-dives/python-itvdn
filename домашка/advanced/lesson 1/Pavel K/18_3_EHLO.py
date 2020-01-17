# 1) откройте клиентский TCP сокет на smtp.gmail.com порт 587
# 2) поздоровайтесь с гуглом, скажите "EHLO google.com" (здесь не опечатка, именно EHLO)
# 3) ответ получите и выведите на экран
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('smtp.gmail.com', 587))
text = 'EHLO google.com\n'
text = str.encode(text)
result = sock.recv(1024)
print('OUT PUT: ', result)
sock.send(text) # в байты можно было преобразовать еще вот так sock.send(b'EHLO google.com\n')
result = sock.recv(1024)
print('OUT PUT: ', result)

sock.close()

# OUT PUT:  b'220 smtp.gmail.com ESMTP x84sm12002146lfa.97 - gsmtp\r\n'
# OUT PUT:  b'250-smtp.gmail.com at your service, [185.143.147.208]\r\n250-SIZE 35882577\r\n250-8BITMIME\r\n250-STARTTLS\r\n250-ENHANCEDSTATUSCODES\r\n250-PIPELINING\r\n250-CHUNKING\r\n250 SMTPUTF8\r\n'
