import platform

import aiohttp
import asyncio
from datetime import datetime, timedelta
from typing import List

# https://api.privatbank.ua/p24api/exchange_rates?json&date=01.12.2014
BASE_URL = 'https://api.privatbank.ua/p24api/exchange_rates'
# BASE_URL = 'https://test'


async def request(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    json = await resp.json()
                    return json
                else:
                    return {'errorStatus': resp.status, 'details': await resp.text()}
        except aiohttp.ClientConnectorError as err:
            return {'errorStatus': err.errno, 'details': err}


def get_dates(total_days=7) -> List[str]:
    result_ = []
    today = datetime.now()
    for d in range(total_days):
        date_ = today - timedelta(days=d)
        str_date = datetime.strftime(date_, '%d.%m.%Y')
        result_.append(str_date)
    result_.append('err_date')
    return result_


def adapter_response(response):
    exchange_rate = response['exchangeRate']
    rates = list(filter(lambda el: el.get('currency', None) in ['EUR', 'USD'], exchange_rate))
    rates = list(map(lambda el: {
        el.get('currency', None): {'sale': el.get('saleRate', None), 'purchase': el.get('purchaseRate', None)}
    }, rates))
    result = {}
    for el in rates:
        result.update(el)
    return result


async def get_rate(date: str) -> dict:
    url = f'{BASE_URL}?json&date={date}'
    response = await request(url)
    if 'exchangeRate' in response:
        return {date: adapter_response(response)}
    return {date: response}


async def main(dates):
    # tasks = [asyncio.create_task(get_rate(date)) for date in dates]
    # print(tasks)
    # result = await asyncio.gather(*tasks, return_exceptions=True)

    cors = [get_rate(date) for date in dates]
    print(cors)
    result = await asyncio.gather(*cors, return_exceptions=True)

    return result


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    dates = get_dates(2)
    r = asyncio.run(main(dates))
    print(r)
