import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(("127.0.0.1", 1500))
    while True:
        message = input(">>  ").encode("utf-8")
        sock.send(message)

except ConnectionRefusedError:
    print()
    print("Server is not on-line")
    exit()
