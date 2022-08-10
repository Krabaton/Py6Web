import asyncio
from contextvars import ContextVar

global_name: ContextVar[str | None] = ContextVar('global_name', default=None)


async def task(name: str):
    print(f'My name {name}: {global_name.get()}')
    global_name.set(name)
    print(f'My name {name}: {global_name.get()}')


async def main():
    futures = [task(name) for name in ['Yulya', 'Vova', 'Nata']]
    await asyncio.gather(*futures)


if __name__ == '__main__':
    asyncio.run(main())