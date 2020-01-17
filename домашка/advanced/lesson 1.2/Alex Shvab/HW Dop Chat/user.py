import socket
import threading


def read_sok():
    while 1:
        data = s.recv(1024)
        print(data.decode('utf-8'))


server = ('127.0.0.1', 5050)
alias = input("Enter your name: ")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(server)
s.sendto((alias + ' Connect to server').encode('utf-8'), server)
thread = threading.Thread(target=read_sok)
thread.start()
while 1:
    msg = input()
    s.sendto(('[' + alias + ']' + msg).encode('utf-8'), server)
