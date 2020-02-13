import asyncio

RESULT = []


async def coro():
    reader, writer = await asyncio.open_connection("localhost", 9999)
    writer.write(b"Taras")
    await writer.drain()

    data = await reader.read()
    tmp = int(data.decode())
    RESULT.append(tmp)
    if sum(RESULT) == 50:
        tmp = str(sum(RESULT))
        writer.write(tmp.encode())
        await writer.drain()
    writer.close()
    await writer.wait_closed()


loop = asyncio.get_event_loop()
coroutine1 = coro()
coroutine2 = coro()
coroutine3 = coro()
coroutine4 = coro()
coroutine5 = coro()
task1 = loop.create_task(coroutine1)
task2 = loop.create_task(coroutine2)
task3 = loop.create_task(coroutine3)
task4 = loop.create_task(coroutine4)
task5 = loop.create_task(coroutine5)
loop.run_until_complete(asyncio.wait([task1, task2, task3, task4, task5]))
loop.close()

