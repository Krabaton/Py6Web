from threading import Thread
import logging
from time import sleep


def example_work(params):
    sleep(0.5)
    logging.debug(params)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    threads = []
    for i in range(5):
        thread = Thread(target=example_work, args=(f"Count thread - {i}",))  # daemon=True
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]

    logging.debug('End program')
