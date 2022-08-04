from multiprocessing import Process, Condition
from time import sleep


def worker(condition: Condition):
    print('Run event work')
    with condition:
        condition.wait()
        print('Хозяин подарил Доби носок! Можно работать')


def master(condition: Condition):
    print('Master делает тяжелую работу')
    with condition:
        print('Даем разрешение работать остальным')
        condition.notify_all()


if __name__ == '__main__':
    condition = Condition()
    master_one = Process(name='master', target=master, args=(condition, ))

    worker_one = Process(target=worker, args=(condition, ))
    worker_two = Process(target=worker, args=(condition, ))
    worker_one.start()
    worker_two.start()

    sleep(5)
    master_one.start()

    print('End program')