# Задание 2
# Создайте UDP клиента, который будет отправлять уникальный идентификатор устройства на сервер,
# уведомляя о своем присутствии.


# UDP client socket
import socket


def main():
    # создаем UDP socket (IP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # цикл ввода и отправки сообщений на сервер
    while True:
        msg = input('Введите сообщение на сервер: ')
        msgb = msg.encode('utf-8')

        # отправляем сообщение на `127.0.0.1:7777`
        sock.sendto(msgb, ('127.0.0.1', 7777))

        # проверка необходимости выхода из цикла
        if msg.strip().lower() == "stope":
            break


if __name__ == '__main__':
    main()