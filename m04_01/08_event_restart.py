from threading import Thread, Event
import logging
from time import sleep


def example_work(event_for_exit: Event):
    while True:
        sleep(1)
        if event_for_exit.is_set():
            continue
        else:
            logging.debug('Run event work')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    event = Event()
    thread = Thread(target=example_work, args=(event,), daemon=True)
    thread.start()
    logging.debug('Start!')
    sleep(3)
    logging.debug('Stop!')
    event.set()
    sleep(3)
    logging.debug('Start!')
    event.clear()
    sleep(3)
    logging.debug('Stop!')
    event.set()
    logging.debug('End program')
