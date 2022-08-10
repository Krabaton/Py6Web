import asyncio
from time import time


async def send_metrics(url):
    print(f'Send to {url}: {time()}')


async def worker():
    while True:
        await asyncio.sleep(2)
        await send_metrics('https://to.me')


if __name__ == '__main__':
    # asyncio.run(worker())
    loop = asyncio.get_event_loop()
    loop.create_task(worker())
    loop.run_forever()
