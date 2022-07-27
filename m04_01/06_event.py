from threading import Thread, Event
import logging
from time import sleep


def example_work(event: Event):
    logging.debug('Run event work')
    event.wait()
    logging.debug('Flag event is true')


def example_work_timeout(event: Event, time: float):
    while not event.is_set():
        logging.debug('Ждем пока не установится флаг event')
        event_wait = event.wait(time)
        logging.debug('Наш флаг установлен?')
        if event_wait:
            logging.debug('Начинаем работать по сигналу')
        else:
            logging.debug('Все еще ждем пока не установится флаг event')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    event = Event()
    thread = Thread(target=example_work, args=(event,))
    thread.start()

    thread_timeout = Thread(target=example_work_timeout, args=(event, 1))
    thread_timeout.start()

    sleep(5)
    event.set()

    logging.debug('End program')
