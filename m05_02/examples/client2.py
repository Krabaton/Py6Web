import time
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager


def worker(qu: Queue, message: str):
    qu.put(message)


BaseManager.register('get_qu')
manager = BaseManager(address=('127.0.0.1', 5000), authkey=b'abc')

if __name__ == '__main__':
    manager.connect()
    qu = manager.get_qu()
    for i in range(10):
        wrk = Process(target=worker, args=(qu, f'Spam message {i}'))
        wrk.start()
        wrk.join()
