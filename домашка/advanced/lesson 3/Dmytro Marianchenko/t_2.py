# не понял, как события должны маячить друг другу...

import time
import threading

w = "Wow!"
content = None
reader_text = None


def open_file():
    global reader_text
    while True:
        try:
            with open("text.txt", "r") as file:
                reader_text = file.read()
                print("I find the file")
                run_p2.start()
                break
        except FileNotFoundError:
            print("No such file.. keep looking...")
            time.sleep(5)
            print("Again...")
            pass


def search():
    global reader_text
    while True:
        if "Wow!" in reader_text:
            print("I find it!")
            run_p3.start()
            break
        else:
            print("No such text in file.. keep looking...")
            time.sleep(5)
            print("Again...")
            continue


def delete_file():
    import os
    os.remove("text.txt")


ev = threading.Event()
run_p1 = threading.Thread(target=open_file)
run_p2 = threading.Thread(target=search)
run_p3 = threading.Thread(target=delete_file)

run_p1.start()
