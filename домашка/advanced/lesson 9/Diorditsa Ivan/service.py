import socketserver
import threading
import random

clients = dict()
clients_lock = threading.Lock()


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        try:
            word = self.request.recv(10).decode()
            print(f'got client, {word=}')

            clients_lock.acquire()
            client = clients.setdefault('word', {'cond': threading.Condition(), 'count': 0, 'sum': 0})
            clients_lock.release()

            num = random.randint(0, 100)
            client['cond'].acquire()
            client['count'] += 1
            if client['count'] < 5:
                client['cond'].wait()
            else:
                client['cond'].notify_all()
            client['sum'] += num
            sum = client['sum']
            client['cond'].release()

            print(f'sent {num=} to {word=}, {sum=}')
            self.request.send(f"{num}".encode())
        except Exception as ex:
            print(ex)


class MyTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    request_queue_size = 10

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 10000

    # Create the server, binding to localhost on port 9999
    with MyTCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
