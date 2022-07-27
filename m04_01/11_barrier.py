from random import randint
from threading import Thread, Barrier, current_thread
import logging
from time import sleep, ctime


def worker(barrier: Barrier):
    name = current_thread().name
    logging.debug(f'Start thread {name}: {ctime()}')
    sleep(randint(1, 3))  # Имитируем какую-то работу
    barrier.wait()
    logging.debug(f'Барьер преодолен для {name}')
    logging.debug(f'End work thread {name}: {ctime()}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    barrier = Barrier(5)

    for num in range(10):
        thread = Thread(name=f'Th-{num}', target=worker, args=(barrier, ))
        thread.start()

    logging.debug('End program')
