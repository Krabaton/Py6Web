from datetime import datetime


class Event:
    _observers = []

    @classmethod
    def register(cls, observer):  # attach, on
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def unregister(cls, observer):  # detach, off
        if observer in cls._observers:
            cls._observers.remove(observer)

    @classmethod
    def notify(cls, event, data=None):  # emit
        for observer in cls._observers:
            observer(event, data)


def logging(event, data):
    print(f'<{event}>: {data}')


class WriteLogs:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, event, data):
        with open(self.filename, 'a') as flog:
            flog.write(f"{datetime.now()}: [{event}]: {data}\n")


if __name__ == '__main__':
    file_logs = WriteLogs('logs.txt')
    Event.register(logging)
    Event.register(file_logs)
    num = int(input('Input integer number (for exit 0): '))
    while True:
        if num == 0:
            break
        if num == 16:
            Event.unregister(logging)
        if num % 2 == 0:
            Event.notify('EVEN', num)

        num = int(input('Input integer number (for exit 0): '))