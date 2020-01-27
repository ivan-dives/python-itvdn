# Создайте три функции, одна из которых читает файл на диске с заданным именем и проверяет
# наличие строку “Wow! ”. В случае, если файла нет, то засыпает на 5 секунд, а затем снова
# продолжает поиск по файлу. В случае, если файл есть, то открывает его и ищет строку “Wow!”. При
# наличии данной строки закрывает файл и генерирует событие, а другая функция ожидает данное
# событие и в случае его возникновения выполняет удаление этого файла. В случае если строки
# «Wow!» не было найдено в файле, то засыпать на 5 секунд. Создайте файл руками и проверьте
# выполнение программы.
import threading
import time
import os


def find():
    try:
        with open('testfile.txt', 'r') as wow:
            print('File found.')
            if 'Wow!' in wow.read():
                print('"Wow!" was found in "testfile.txt"')
                my_event.set()
            else:
                print('"Wow!" was not found in "testfile.txt"')
                time.sleep(5)

    except FileNotFoundError:
        print('File "testfile.txt" has not found.')
        time.sleep(5)
        find()


def wait_wow():
    my_event.wait()
    os.remove('testfile.txt')
    print('File deleted.')


my_event = threading.Event()

task1 = threading.Thread(target=find)
task2 = threading.Thread(target=wait_wow)

task1.start()
task2.start()

task1.join()
task2.join()
