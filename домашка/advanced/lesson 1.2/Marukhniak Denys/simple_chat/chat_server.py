# Создать простой чат, на основе TCP протокола, который позволит подключаться нескольким клиентам и обмениваться
# сообщениями.
import socketserver


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        msg = self.request.recv(64)
        msg = msg.decode()
        name, text = msg.split(sep=': ')[0], msg.split(sep=': ')[1]
        print(f'Received from {name}: {text}')
        msg = name + ': ' + text
        self.request.send(msg.encode())


if __name__ == '__main__':
    with ThreadingTCPServer(('localhost', 10000), EchoTCPHandler) as server:
        server.serve_forever()
