import asyncio

SRV_IP = "192.168.88.39"
SRV_PORT = 10000
MAX_NUM = 5
num_lst = []


async def get_num():
    print('get_num started')
    reader, writer = await asyncio.open_connection(SRV_IP, SRV_PORT)
    writer.write(b"osm")
    await writer.drain()

    data = await reader.read()
    curr_num = int(data.decode())
    print(f'{len(num_lst)}: {curr_num}')
    num_lst.append(curr_num)

    writer.close()
    await writer.wait_closed()


async def wait_maxnum(max_num):
    print('wait_maxnum started')
    reader, writer = await asyncio.open_connection(SRV_IP, SRV_PORT)

    while len(num_lst) < max_num:
        await asyncio.sleep(5)

    sum_lst = 0
    for i in num_lst:
        sum_lst += i

    print(f'sum_lst = {sum_lst}')
    res = f'osm={sum_lst}'
    writer.write(res.encode())
    await writer.drain()

    writer.close()
    await writer.wait_closed()

def main():
    loop = asyncio.get_event_loop()
    f1 = get_num()
    f2 = wait_maxnum(MAX_NUM)
    for i in range(MAX_NUM):
        loop.create_task(f1)
    loop.create_task(f2)
    loop.run_forever()


if __name__ == '__main__':
        main()
