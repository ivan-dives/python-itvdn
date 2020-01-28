# Создайте три функции, одна из которых читает файл на диске с заданным именем и проверяет наличие строку “Wow! ”. В случае, если файла нет,
# то засыпает на 5 секунд, а затем снова продолжает поиск по файлу. В случае, если файл есть, то открывает его и ищет строку “Wow!”.
# При наличии данной строки закрывает файл и генерирует событие, а другая функция ожидает данное событие и в случае его возникновения выполняет удаление этого файла.
# В случае если строки «Wow!» не было найдено в файле, то засыпать на 5 секунд. Создайте файл руками и проверьте выполнение программы.

import threading
import time
import os


def search_file():
    try:
        f = open('123.txt', 'r')
        print('Поиск по файлу')
        if 'Wow!' in f.read():
            time.sleep(5)
            print('"Wow!" есть в "123.txt"')
            event1.set()

        else:
            time.sleep(5)
            print('"Wow!" нету в  "123.txt" Через 5 секунд будет новая проверка файла.')
            search_file()

    except FileNotFoundError:
        print('файл не найден. Через 5 секунд будет новая проверка файла "123.txt"')
        time.sleep(5)
        print()
        search_file()


def del_file():
    event1.wait()
    os.remove('123.txt')
    print('Файл удален.')

event1 = threading.Event()

task1 = threading.Thread(target=search_file)
task2 = threading.Thread(target=del_file)

task1.start()
task2.start()

task1.join()
task2.join()