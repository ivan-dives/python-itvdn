import io
import http.client
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        #while True:
        #    bts = self.request.recv(100000)
        #    print(bts.decode())
        #    self.request.send(b'HTTP/1.1 200 OK\r\n\r\n')
        bts = self.request.recv(100000)
        print(f"{len(bts)=}")
        f = io.BytesIO(bts)
        print(f"before parse_headers: {f.tell()=}")
        headers = http.client.parse_headers(f)
        print(f"after parse_headers: {f.tell()=}")
        headers = str(headers).split('\n')
        print(f"{headers=}")
        for h in headers:
            try:
                name, value = h.split(': ')
                if name == 'Content-Type' and value != 'image/jpeg':
                    return
                if name == 'Content-Length':
                    length = int(value)
                    img = f.read(length)
                    with open("image.jpg", 'wb') as img_f:
                        img_f.write(img)
            except ValueError:
                pass

class MyTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    request_queue_size = 10


ss = MyTCPServer(('localhost', 20000), MyTCPHandler)
ss.serve_forever()
