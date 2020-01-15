import socket

text = input('Enter message: ')

r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect(('127.0.0.1', 10000))
r.send(text.encode('utf-8'))

r.close()