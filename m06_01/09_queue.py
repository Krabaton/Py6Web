import asyncio
import random
import queue


async def producer(queue: asyncio.Queue):
    num = random.randint(1, 100)
    await asyncio.sleep(0.3)
    await queue.put(num)


async def consumer(queue: asyncio.Queue, result: queue.Queue):
    while True:
        num = await queue.get()
        r = num ** 2
        result.put((num, r))
        queue.task_done()


async def main():
    queue_async = asyncio.Queue()
    queue_sync = queue.Queue()

    producers = [asyncio.create_task(producer(queue_async)) for _ in range(10)]  # ensure_future like as create_task
    consumers = [asyncio.create_task(consumer(queue_async, queue_sync)) for _ in range(5)]

    await asyncio.gather(*producers)
    await queue_async.join()
    for consume in consumers:
        consume.cancel()

    while not queue_sync.empty():
        print(queue_sync.get())


if __name__ == '__main__':
    asyncio.run(main())
