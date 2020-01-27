import threading
import time
import os


def wow_check():
    wow = "Wow!"
    while True:
        try:
            print("try open")
            with open("wow.txt", "r") as file:
                print("Read")
                res = file.read()
                if wow in res:
                    print("Find")
                    product.set()
                    product.clear()
                    break
                else:
                    time.sleep(1)
        except FileNotFoundError:
            time.sleep(1)
        except Exception as e:
            print(f'Unexpected error occurred!')
            print(e)


    # time.sleep(10)
    # print('Product found!')
    # # устанавливаем событий
    # product.set()
    # # очищаем событие
    # product.clear()


def find_wow():
    while True:
        print("listen")
        product.wait()
        try:
            os.remove("wow.txt")
            print("Delete")
            break
        except FileNotFoundError:
            pass


    # print('product wait')
    # # ожидаем события ровно столько, пока не вызовется product.set в любом из
    # # потоков
    # product.wait()
    # print('Product exists!')


# создаем событие, которое будем использовать в потока- ожидать и устанавливать
# создадим блокировку потока до появления события product
product = threading.Event()

task1 = threading.Thread(target=wow_check)
task2 = threading.Thread(target=find_wow)

task1.start()
task2.start()

task1.join()
task2.join()
