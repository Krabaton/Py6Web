from multiprocessing import Process


def baz(n, cb):
    sum = 0
    for i in range(n):
        sum += i
    cb(sum)  # callback(sum)


def callback(result):
    print(result)


if __name__ == '__main__':
    pr = Process(target=baz, args=(10, callback))
    pr.start()
