from threading import Thread, Semaphore, RLock, current_thread
import logging
from time import sleep


class Pool:
    def __init__(self):
        self.active = []
        self.lock = RLock()

    def make_active(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug(f'Начал работу поток {name}. Сейчас в пуле потоки {self.active}')

    def make_inactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug(f'Закончил работу поток {name}. Сейчас в пуле потоки {self.active}')


def worker(semaphore: Semaphore, pool: Pool):
    logging.debug('Wait')
    with semaphore:
        name = current_thread().name
        pool.make_active(name)
        sleep(0.2)  # Имитируем какую-то работу
        pool.make_inactive(name)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    semaphore = Semaphore(3)
    pool = Pool()
    for num in range(10):
        thread = Thread(name=f'Th-{num}', target=worker, args=(semaphore, pool))
        thread.start()

    logging.debug('End program')
