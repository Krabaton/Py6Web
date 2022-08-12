import aiohttp
import asyncio
import platform

urls = ['http://www.google.com', 'http://www.python.org/asdf', 'http://duckduckgo.com', 'http://test']


async def main():
    async with aiohttp.ClientSession() as session:
        for url in urls:
            try:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        html = await resp.text()
                        print(html[:150])
                    else:
                        print(resp.status)
            except aiohttp.ClientConnectorError as err:
                print(f'Connection error: {url}', str(err))


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
