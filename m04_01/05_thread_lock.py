from random import randint
from threading import Thread, RLock
import logging
from time import sleep

counter = 0
lock = RLock()


def example_work():
    global counter
    while True:
        # lock.acquire()
        with lock:
            counter = counter + 1
            sleep(randint(1, 3))
            with open('result.txt', 'a') as fa:
                fa.write(f'{counter}\n')
        # lock.release()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    logging.debug('Start program')
    for i in range(5):
        thread = Thread(target=example_work)  # daemon=True
        thread.start()

    logging.debug('End program')