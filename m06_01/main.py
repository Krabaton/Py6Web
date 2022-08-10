import asyncio
import aiohttp
import platform

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com']


async def call_url(url):
    print(f'Starting {url}')
    session = aiohttp.ClientSession()
    response = await session.get(url)
    data = await response.text()
    print(f'{url} bytes:{len(data)} {data[:200]}')
    await session.close()
    return data


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    futures = [call_url(url) for url in urls]
    results = loop.run_until_complete(asyncio.gather(*futures))
    loop.close()