import asyncio
from faker import Faker
from typing import Coroutine, List

fake = Faker()


async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)
    return {'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


async def get_users() -> List[Coroutine]:
    return [get_user_async(1), get_user_async(2), get_user_async(3)]


async def main(users):
    result = []
    for user in await users:
        result.append(await user)
    return result


if __name__ == '__main__':
    r = asyncio.run(main(get_users()))
    print(r)

