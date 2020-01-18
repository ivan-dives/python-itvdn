import select
import socket

def run_server():
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.bind(('localhost', 20004))
    srv_sock.listen(10)

    all_sockets = [srv_sock]

    while True:
        r, w, e = select.select(all_sockets, [], [], 1)
        for s in r:
            print(f'{s=}')
            if s is srv_sock: # new client
                user_sock, addr = s.accept()
                print(f'accepted {addr=}')
                all_sockets.append(user_sock)
            else:
                buffer = s.recv(1024)
                for i in all_sockets:
                    if (i is srv_sock) or (i is s):
                        continue
                    i.send(buffer)


def run_client():
    import sys

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('localhost', 20004))
    while True:
        r, w, e = select.select([client_sock, sys.stdin], [], [], 1)
        #print(f'{r=}')
        if client_sock in r:
            buffer = client_sock.recv(1024)
            buffer = buffer.decode('utf-8')
            print(buffer)
        if sys.stdin in r:
            buffer = sys.stdin.readline()
            #input()
            #print(f'from stdin read {buffer=}')
            client_sock.send(buffer.encode('utf-8'))


if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 2 and sys.argv[1] == '-c':
        run_client()
    else:
        run_server()