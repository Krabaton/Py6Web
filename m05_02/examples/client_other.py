import sys
from multiprocessing.managers import BaseManager


BaseManager.register('get_qu')
manager = BaseManager(address=('127.0.0.1', 5000), authkey=b'abc')

if __name__ == '__main__':
    manager.connect()
    qu = manager.get_qu()

    while True:
        if not qu.empty():
            print(qu.get())
            # sys.exit(0)
