import socketserver

users = []

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):

        #import traceback
        #traceback.print_stack()

        #self.request.send(f'hello, I am ECHO server, please tell me your name: '.encode())
        #name = self.request.recv(1000)
        #self.request.send(f'hello {name.decode()}'.encode())

        users.append(self)
        print(f"this self is {id(self)}")
        print(f"{self.client_address=}")

        while True:
            b = self.request.recv(1000)
            for user in users:
                if user.client_address != self.client_address:
                    user.request.send(str(user.client_address).encode() + b': ' + b)


class MyTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    request_queue_size = 10


ss = MyTCPServer(('localhost', 10001), MyTCPHandler)
ss.serve_forever()

exit()


import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

