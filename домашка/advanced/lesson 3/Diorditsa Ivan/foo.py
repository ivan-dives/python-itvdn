import asyncio

x = 10


def coro():
    while True:
        yield


async def foo():
    global x

    while True:
        print("called foo")
        x += 1
        await asyncio.sleep(0.01)


async def bar():
    global x

    while True:
        print("called bar")
        x -= 1
        await asyncio.sleep(0.01)


async def printer():
    global x

    while True:
        print(x)
        await asyncio.sleep(0.02)


async def main():
    while True:
        await asyncio.gather(foo(), bar(), printer())

asyncio.run(main())


exit()

import threading
import time

x = 10
lock = threading.Lock()


def foo():
    global x

    while True:
        lock.acquire()
        y = x
        y += 1
        time.sleep(0)
        x = y
        lock.release()
        print(f"foo {y=}")


def bar():
    global x

    while True:
        lock.acquire()
        y = x
        y -= 1
        time.sleep(0)
        x = y
        lock.release()
        print(f"bar {y=}")


t1 = threading.Thread(target=foo, kwargs=None)
t2 = threading.Thread(target=bar, kwargs=None)
t1.start()
t2.start()


exit()
