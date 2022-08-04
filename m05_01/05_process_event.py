from multiprocessing import Process, Event
from time import sleep


def example_work(event: Event):
    print('Run event work')
    event.wait()
    print('Flag event is true')


def example_work_timeout(event: Event, time: float):
    while not event.is_set():
        print('Ждем пока не установится флаг event')
        event_wait = event.wait(time)
        print('Наш флаг установлен?')
        if event_wait:
            print('Начинаем работать по сигналу')
        else:
            print('Все еще ждем пока не установится флаг event')


if __name__ == '__main__':
    event = Event()
    pr = Process(target=example_work, args=(event,))
    pr.start()

    pr_timeout = Process(target=example_work_timeout, args=(event, 1))
    pr_timeout.start()

    sleep(5)
    event.set()

    print('End program')