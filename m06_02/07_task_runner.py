import asyncio
from pathlib import Path
from aiofile import async_open


async def producer(filename: Path, queue: asyncio.Queue):
    async with async_open(filename, "r", encoding='utf-8') as afp:
        print(f'read file: {filename.name}')
        data = []
        async for line in afp:
            data.append(str(line))
        data_all = ''.join(data)
        await queue.put((filename, data_all))
        print(f'completed file: {filename.name}')


async def consumer(filename: str, queue: asyncio.Queue):
    async with async_open(filename, "w", encoding='utf-8') as afp:
        while True:
            file, data = await queue.get()
            print(f'Start concat file: {file.name}')
            await afp.write(f'{data}\n')
            queue.task_done()


async def main(files):
    queue = asyncio.Queue()

    producers = [asyncio.create_task(producer(file, queue)) for file in files]  # ensure_future like as create_task
    consume = asyncio.create_task(consumer('main.js', queue))

    await asyncio.gather(*producers)
    await queue.join()
    consume.cancel()
    print('Done')


if __name__ == '__main__':
    list_files = Path('.').joinpath('files').glob('*.js')
    asyncio.run(main(list_files))
