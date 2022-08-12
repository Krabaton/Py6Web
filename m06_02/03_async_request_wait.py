import asyncio
import requests
from concurrent.futures import ProcessPoolExecutor
from time import time
from random import random

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com']  # , 'http://test'


def preview_fetch(url):
    r = requests.get(url)
    if random() > 0.5:
        raise Exception('Sometimes shit happened...')
    return url, r.text[:150]


async def preview_fetch_async():
    loop = asyncio.get_running_loop()
    
    with ProcessPoolExecutor(2) as pool:
        futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]
        done, pending = await asyncio.wait(futures)  # , return_when=asyncio.FIRST_COMPLETED
        print('Done: ', done)
        print('Pending: ', pending)

        [el.cancel() for el in pending]

        r = []
        for core in done:
            try:
                r.append(await core)
            except Exception as err:
                print(err)

        return r


if __name__ == '__main__':
    start = time()
    r = asyncio.run(preview_fetch_async())
    print(r)
    print(time() - start)
