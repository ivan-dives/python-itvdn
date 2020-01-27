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



product = threading.Event()

task1 = threading.Thread(target=wow_check)
task2 = threading.Thread(target=find_wow)

task1.start()
task2.start()

task1.join()
task2.join()
