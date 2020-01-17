import socketserver
import time

class ThreadingTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        time.sleep(100)
        print('received', data)


if __name__ == '__main__':
    with ThreadingTCPServer(('', 10000), EchoTCPHandler) as server:
        server.serve_forever()

exit()

import socketserver
import time


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        #data = self.request.recv(1024).strip()
        #print('Address: {}'.format(self.client_address[0]))
        #print('Data: {}'.format(data.decode()))
        #self.request.sendall(data)

        msg = self.request.recv(1000)
        #time.sleep(10)
        print('received', msg)


if __name__ == '__main__':
    with socketserver.TCPServer(('', 10000), EchoTCPHandler) as server:
        server.serve_forever()