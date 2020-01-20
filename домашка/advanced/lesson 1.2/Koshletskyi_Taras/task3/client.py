#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'15, 25', ('127.0.0.1', 10001))
data, server = sock.recvfrom(4096)
print(data.decode("utf-8"))