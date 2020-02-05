# как заливать картинку

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 20000))

with open("/home/ivan/ASF20thAnniversary.jpg", "rb") as img_f:
    img = img_f.read()

req = f"""\
POST / HTTP/1.1\r
Content-Type: image/jpeg\r
Content-Length: {str(len(img))}\r
\r
"""

print(f"{len(req)=}")

req_b = req.encode()
req_b += img

s.send(req_b)
s.close()
