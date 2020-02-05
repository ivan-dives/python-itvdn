import io
import http.client
import socketserver


class MyTCPHendler(socketserver.BaseRequestHandler):
    def GET(self):
        with open("ok.jpg", "rb") as img_f:
            img = img_f.read()

        req = f"""\
        POST / HTTP/1.1\r
        Content-Type: image/jpeg\r
        Content-Length: {str(len(img))}\r
        \r
        """

        req_b = req.encode()
        req_b += img

        s.send(req_b)

    def POST(self):
        msg_bts = self.request.recv(100000)
        f = io.BytesIO(msg_bts)
        headers = http.client.parse_headers(f)
        headers = str(headers).split("\n")
        for h in headers:
            try:
                name, value = h.split(": ")
                if name == "Content-Type" and value != "image/jpeg":
                    return
                if name == "Content-Length":
                    length = int(value)
                    image = f.read(length)
                    with open("image.jpg", "wb") as img_file:
                        img_file.write(image)
            except ValueError:
                pass



class MyTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    request_queue_size = 10

service = MyTCPServer(("127.0.0.1", 20000), MyTCPHendler)
service.serve_forever()


#
