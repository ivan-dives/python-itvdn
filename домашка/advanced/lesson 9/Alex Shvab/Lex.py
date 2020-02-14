import asyncio


numbers = []
result = "Alians = "


async def take_namer():
    reader, writer = await asyncio.open_connection("192.168.88.39", 10000)
    writer.write(b"Jgy")
    await writer.drain()
    data = await reader.read()
    numbers.append(data)
    writer.close()
    await writer.wait_closed()


loop = asyncio.new_event_loop()
car1 = take_namer()
car2 = take_namer()
car3 = take_namer()
car4 = take_namer()
car5 = take_namer()
task1 = loop.create_task(car1)
task2 = loop.create_task(car2)
task3 = loop.create_task(car3)
task4 = loop.create_task(car4)
task5 = loop.create_task(car5)
loop.run_until_complete(asyncio.wait([task1, task2, task3, task4, task5]))


async def sum():
    res = 0
    for i in numbers:
        res += int(i)
    global result
    result = result + str(res)
    reader, writer = await asyncio.open_connection("192.168.88.39", 10000)
    print(result)
    await writer.drain()
    writer.close()


loop = asyncio.new_event_loop()
car6 = sum()
task6 = loop.create_task(car6)
loop.run_until_complete(asyncio.wait([task6]))
loop.close()
