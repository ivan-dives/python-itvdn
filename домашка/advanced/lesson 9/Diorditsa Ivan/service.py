import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # (b'text', <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=0, laddr=('127.0.0.1', 9999)>)
        # print(self.request[0].decode())
        # self.request[1].sendto(b"PASSWORD ACCEPTED", self.client_address)
        # import time
        # time.sleep(3)
        # self.request[1].sendto(b"your balance is 1000 UAH", self.client_address)
        # return

        # self.request is the TCP socket connected to the client
        # self.data = self.request.recv(1024).strip()
        # print("{} wrote:".format(self.client_address[0]))
        # print(self.data)
        # # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())

        print(self.request.recv(1024).decode())
        self.request.send(b'ACCEPTED')

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()