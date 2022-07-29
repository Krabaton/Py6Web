import requests
from datetime import datetime, timedelta
from typing import List

# https://api.privatbank.ua/p24api/exchange_rates?json&date=01.12.2014
BASE_URL = 'https://api.privatbank.ua/p24api/exchange_rates'


def get_dates(total_days=7) -> List[str]:
    result_ = []
    today = datetime.now()
    for d in range(total_days):
        date_ = today - timedelta(days=d)
        str_date = datetime.strftime(date_, '%d.%m.%Y')
        result_.append(str_date)
    return result_


def get_rate(date: str) -> dict:
    url = f'{BASE_URL}?json&date={date}'
    response = requests.get(url)
    exchange_rate = response.json()['exchangeRate']
    rates = list(filter(lambda el: el.get('currency', None) in ['EUR', 'USD'], exchange_rate))
    rates = list(map(lambda el: {
        el.get('currency', None): {'sale':  el.get('saleRate', None), 'purchase':  el.get('purchaseRate', None)}
    }, rates))
    result = {}
    for el in rates:
        result.update(el)
    return result


if __name__ == '__main__':
    dates = get_dates(2)
    rate_result = []
    for date in dates:
        r = get_rate(date)
        rate_result.append({date: r})

    print(rate_result)

