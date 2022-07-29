import requests
from datetime import datetime, timedelta
from typing import List
from queue import Queue, Empty
from threading import Thread

# https://api.privatbank.ua/p24api/exchange_rates?json&date=01.12.2014
BASE_URL = 'https://api.privatbank.ua/p24api/exchange_rates'
THREAD_POOL_SIZE = 2


def get_dates(total_days=7) -> List[str]:
    result_ = []
    today = datetime.now()
    for d in range(total_days):
        date_ = today - timedelta(days=d)
        str_date = datetime.strftime(date_, '%d.%m.%Y')
        result_.append(str_date)
    result_.append('err_date')
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


def worker(work_queue, results_queue):
    while not work_queue.empty():
        try:
            date_ = work_queue.get(block=False)
        except Empty:
            break
        else:
            results_queue.put({date_: get_rate(date_)})
            work_queue.task_done()


if __name__ == '__main__':
    work_queue = Queue()  # для дат
    results_queue = Queue()  # для результатов

    dates = get_dates(2)

    for date in dates:
        work_queue.put(date)

    threads = [Thread(target=worker, args=(work_queue, results_queue)) for _ in range(THREAD_POOL_SIZE)]

    [thread.start() for thread in threads]

    work_queue.join()

    while threads:
        threads.pop().join()

    while not results_queue.empty():
        r = results_queue.get()
        print(r)

