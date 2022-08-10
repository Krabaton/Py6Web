import asyncio
from time import sleep, time
from faker import Faker

fake = Faker()


async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)
    return {'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


async def get_users():
    u1 = asyncio.create_task(get_user_async(1))
    u2 = asyncio.create_task(get_user_async(2))
    u3 = asyncio.create_task(get_user_async(3))

    return await u1, await u2, await u3


if __name__ == '__main__':
    start = time()
    # loop = asyncio.get_event_loop()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    r = loop.run_until_complete(get_users())
    print(r)
    print(time() - start)
    loop.close()

