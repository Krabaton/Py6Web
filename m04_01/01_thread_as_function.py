from threading import Thread


def example_work(params):
    print(params)


if __name__ == '__main__':
    for i in range(5):
        thread = Thread(target=example_work, args=(f"Count thread - {i}",))
        thread.start()
