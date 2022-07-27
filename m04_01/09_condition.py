from threading import Thread, Condition
import logging
from time import sleep


def worker(condition: Condition):
    logging.debug('Run event work')
    with condition:
        condition.wait()
        logging.debug('Хозяин подарил Доби носок! Можно работать')


def master(condition: Condition):
    logging.debug('Master делает тяжелую работу')
    with condition:
        logging.debug('Даем разрешение работать остальным')
        condition.notify_all()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    condition = Condition()
    master = Thread(name='master', target=master, args=(condition,))

    worker_one = Thread(target=worker, args=(condition, ))
    worker_two = Thread(target=worker, args=(condition,))
    worker_one.start()
    worker_two.start()

    sleep(5)
    master.start()

    logging.debug('End program')
