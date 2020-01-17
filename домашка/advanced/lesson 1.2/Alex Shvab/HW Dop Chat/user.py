import socket
import threading


def read_sok():
    while 1:
        data = s.recv(1024)
        print(data.decode('utf-8'))


server = ('127.0.0.1', 5050)
alias = input("Enter your nickname: ")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 0))
s.sendto((alias + ' Connect to server').encode('utf-8'), server)
thread = threading.Thread(target=read_sok)
thread.start()
while 1:
    message = input()
    s.sendto(('[' + alias + ']' + message).encode('utf-8'), server)
