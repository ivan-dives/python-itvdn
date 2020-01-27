import os
import asyncio

wow = 0


async def wow_seek():
    global wow
    while True:
        wow = 0
        try:
            with open('wow.txt') as f:
                if 'Wow!' in f.read():
                    wow = 1
        except FileNotFoundError:
            await asyncio.sleep(5)
            continue
        except Exception as e:
            print(f'Unexpected error occurred!')
            print(e)
        await asyncio.sleep(5)


async def wow_del():
    global wow
    while True:
        if wow == 1:
            try:
                os.remove('wow.txt')
            except FileNotFoundError:
                pass
            except Exception as e:
                print(f'Unexpected error occurred!')
                print(e)
                await asyncio.sleep(5)
            finally:
                wow = 0
        await asyncio.sleep(0.1)


async def wow_main():
    while True:
        await asyncio.gather(wow_seek(), wow_del())


asyncio.run(wow_main())
