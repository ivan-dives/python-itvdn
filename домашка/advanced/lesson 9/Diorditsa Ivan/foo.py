import asyncio


async def coro():
    reader, writer = await asyncio.open_connection("localhost", 9999)
    writer.write(b"Hello, Name:Ivan, Password:12345")
    await writer.drain()

    data = await reader.read()
    print(data.decode())

    writer.close()
    await writer.wait_closed()

asyncio.run(coro())

exit()

import asyncio
import socket

async def coro():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b"Hi, Name:Ivan, Password:12345", ("localhost", 9999))
    b = s.recv(1024)
    print(b.decode())
    # wait for balance
    s.close()

exit()



#@asyncio.coroutine
#def communicate():
#    reader, writer = yield from asyncio.open_connection(HOST, PORT)
#    writer.write(b'data')
#     yield from writer.drain()
#     answer = yield from reader.read()
#     # process answer, maybe send new data back to server and wait for answer again
#     writer.close()



import asyncio


async def foo():
    print(1)
    await asyncio.sleep(5)
    print(2)

loop = asyncio.get_event_loop()
f = foo()
loop.create_task(f)
loop.run_forever()

exit()


def foo():
    yield 1
    yield 2


f = foo()
print(next(f))
print(next(f))

exit()

import asyncio

loop = asyncio.get_running_loop()
future = loop.run_in_executor()

asyncio.sleep(1)
