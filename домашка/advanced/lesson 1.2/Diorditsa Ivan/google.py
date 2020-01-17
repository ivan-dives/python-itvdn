import select
import socket
import time

smtp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
smtp.connect(('smtp.gmail.com', 587))
r, w, e = select.select([smtp], [], [], 10)
#print(r)
msg = smtp.recv(1000)
print('received from google', msg)
r, w, e = select.select([], [smtp], [], 10)
#print(r, w, e)
smtp.send(b'EHLO google.com\n')
r, w, e = select.select([smtp], [], [], 1)
#print(r, w, e)
#print("HELLO")
msg = smtp.recv(1000)
print('google sent', msg)
smtp.close()
exit()

readable, writable, exceptional = select.select(inputs, outputs, inputs)
#msg = smtp.recv(1000)
#print('google sent', msg)
smtp.send(b'EHLO google.com\n')
time.sleep(1)
msg = smtp.recv(1000)
print('google sent', msg)
smtp.close()

exit()

import socket
import time

smtp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
smtp.connect(('smtp.gmail.com', 587))
#msg = smtp.recv(1000)
#print('google sent', msg)
smtp.send(b'EHLO google.com\n')
time.sleep(1)
msg = smtp.recv(1000)
print('google sent', msg)
smtp.close()