import time
from multiprocessing import Queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


queue = Queue()


def get():
    return queue


QueueManager.register('get_qu', callable=get)

if __name__ == '__main__':
    manager = QueueManager(address=('', 5000), authkey=b'abc')
    server = manager.get_server()
    print('Start server opn port: 5000')
    server.serve_forever()
