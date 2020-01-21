import socket
import sys
import select


server = ('127.0.0.1', 5050)
name = input("Enter your name: ")
user_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_sock.connect(server)

while True:
    r, w, e = select.select([user_sock, sys.stdin], [], [], 1)
    user_sock.send((name + ' Connect to server').encode('utf-8'))
    if user_sock in r:
        msg = user_sock.recv(5000)
        msg = msg.decode("utf-8")
        print(msg)
    if sys.stdin in r:
        msg = sys.stdin.readline()
        user_sock.send(('[' + name + '] ' + msg).encode('utf-8'))
