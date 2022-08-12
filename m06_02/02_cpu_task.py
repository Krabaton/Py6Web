import asyncio
from concurrent.futures import ProcessPoolExecutor
from time import time
import datetime


def blocking_task():
    counter = 50_000_000
    while counter > 0:
        counter -= 1
    print('End CPU task')


async def worker_async():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor(1) as pool:
        while True:
            f = loop.run_in_executor(pool, blocking_task)
            print(f)
            await f


async def monitoring():
    while True:
        await asyncio.sleep(2)
        print(f'Monitoring {time()}')


async def ticker():
    while True:
        await asyncio.sleep(1)
        print(f'Statistics {datetime.datetime.now()}')


async def main():
    # blocking_task()
    # blocking_task()
    # blocking_task()
    asyncio.create_task(ticker())
    asyncio.create_task(monitoring())
    asyncio.create_task(worker_async())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()

