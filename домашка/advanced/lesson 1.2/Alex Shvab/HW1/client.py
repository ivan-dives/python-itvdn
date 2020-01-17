import socket


numbers = input("Enter 2 numbers separated by ,:")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 10000))
s.send(numbers.encode("utf-8"))
msg = s.recv(100).decode()
print(f"Result {msg}")
s.close()
