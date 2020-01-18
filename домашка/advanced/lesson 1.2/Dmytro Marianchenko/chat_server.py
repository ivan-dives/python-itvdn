import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 1500))
sock.setblocking(False)
sock.listen(5)
print("\n...server is on-line...\n")

inputs = [sock]

while True:
    read, write, exceptions = select.select(inputs, [], [])
    for conn in read:
        if conn is sock:
            user, client_address = conn.accept()
            print("server received connection: socket " + str(user.fileno()))
            inputs.append(user)
        else:
            message = conn.recv(1024)
            message = bytes.decode(message)
            print(f"[socket {sock.fileno()}]: {message}")
