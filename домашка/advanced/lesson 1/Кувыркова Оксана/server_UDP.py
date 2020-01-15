from socket import *

host = '127.0.0.1'
port = 10000
addr = (host, port)


udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(addr)

while True:
    question = input('Do you want to quit? y\\n: ')
    if question == 'y':
        break

    print('wait data...')

    conn, addr = udp_socket.recvfrom(1024)
    print('client addr: ', addr)

    udp_socket.sendto(b'message received by the server', addr)

udp_socket.close()