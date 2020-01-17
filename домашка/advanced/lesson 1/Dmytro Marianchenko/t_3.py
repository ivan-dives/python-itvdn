import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("google.com", 80))
sock.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
resp = sock.recv(1024).decode("utf-8")
sock.close()
with open("google_answer.txt", "w") as f:
    f.write(resp)
print()
print("All data from google.com saved to file 'google_answer.txt'")
