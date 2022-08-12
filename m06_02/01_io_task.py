import asyncio
import requests
from concurrent.futures import ProcessPoolExecutor
from time import time

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com', 'http://www.google.com',
        'http://www.python.org', 'http://duckduckgo.com', 'http://www.google.com', 'http://www.python.org',
        'http://duckduckgo.com']


def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[: 150]


async def preview_fetch_async():
    loop = asyncio.get_running_loop()
    
    # with ProcessPoolExecutor(3) as pool:
    #     futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]
    #     r = await asyncio.gather(*futures)
    #     print(r)

    futures = [loop.run_in_executor(None, preview_fetch, url) for url in urls]
    print(futures)
    r = await asyncio.gather(*futures)
    print(r)

if __name__ == '__main__':
    start = time()
    results = []
    for url in urls:
        results.append(preview_fetch(url))
    print(results)
    print(time() - start)

    start = time()
    asyncio.run(preview_fetch_async())
    print(time() - start)
