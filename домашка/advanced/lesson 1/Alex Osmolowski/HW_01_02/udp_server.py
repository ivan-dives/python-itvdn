# Задание 2
# Создайте UDP сервер, который ожидает сообщения о новых устройствах в сети.
# Он принимает сообщения определенного формата, в котором будет идентификатор
# устройства и печатает новые подключения в консоль.


# UDP server socket
import socket

def main():
    # IP UDP-сокет сервер
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(('127.0.0.1', 7777))
    print('UDP-server started')

    # бесконечный цикл для постоянного чтения данных, без остановки сервера
    while True:
        try:
            result = sock.recv(1024)
        except KeyboardInterrupt:
            break
        else:
            rdc = result.decode('utf-8')
            if rdc.strip().lower() == "stope":
                break
            else:
                print('Добавлено устройство:', rdc)
    print('UDP-server finished')
    sock.close()


if __name__ == '__main__':
    main()

