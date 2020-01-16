# Создайте UDP сервер, который ожидает сообщения о новых устройствах в сети. Он принимает сообщения определенного
# формата, в котором будет идентификаторустройства и печатает новые подключения в консоль. Создайте UDP клиента, который
# будет отправлять уникальный идентификатор устройства на сервер, уведомляя о своем присутствии.
import platform
import socket
import os


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name = platform.node()
# name = socket.gethostname()
# name = os.environ['COMPUTERNAME']

name = name.encode()
s.sendto(name, ('127.0.0.1', 10000))
s.close()
exit()
