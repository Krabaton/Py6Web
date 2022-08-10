import asyncio

global_name = None


async def task(name: str):
    global global_name
    print(f'My name {name}: {global_name}')
    global_name = name
    print(f'My name {name}: {global_name}')


async def main():
    futures = [task(name) for name in ['Yulya', 'Vova', 'Nata']]
    await asyncio.gather(*futures)


if __name__ == '__main__':
    asyncio.run(main())