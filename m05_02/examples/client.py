import time
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager


class Worker(Process):
    def __init__(self, qu: Queue):
        self.qu = qu
        super().__init__()

    def run(self):
        self.qu.put('Hello world!')


BaseManager.register('get_qu')
manager = BaseManager(address=('127.0.0.1', 5000), authkey=b'abc')

if __name__ == '__main__':
    manager.connect()
    qu = manager.get_qu()
    wrk = Worker(qu)
    wrk.start()
    wrk.join()
