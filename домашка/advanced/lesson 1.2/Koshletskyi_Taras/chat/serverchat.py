import socketserver



class ChatSever(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print('Address: {} {}'.format(self.client_address[0], self.client_address[1]))
        print('Data: {}'.format(data.decode()))
        self.request.send(b'Test from server')


if __name__ == '__main__':
    with socketserver.TCPServer(('127.0.0.1', 20000), ChatSever) as server:
        server.serve_forever()
