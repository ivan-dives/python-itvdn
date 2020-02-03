import socket
import sys
import select


SERVER = ('127.0.0.1', 20000)
#name = input("Enter your name: ")
user_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_sock.connect(SERVER)

while True:
    r, w, e = select.select([user_sock, sys.stdin], [], [], 1)
    #user_sock.send((name + ' Connect to server').encode('utf-8'))
    if user_sock in r:
        msg = user_sock.recv(1024)
        msg = msg.decode("utf-8")
        print(msg)
    if sys.stdin in r:
        msg = sys.stdin.readline()
        #user_sock.send(('[' + name + '] ' + msg).encode('utf-8'))
        user_sock.send(msg.encode('utf-8'))
