import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        print(self, instance, cls)
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Calculate:
    def __init__(self, x):
        self.x = x

    @Profiled
    def add(self, y):
        return self.x + y


if __name__ == '__main__':
    # add(2, 3)
    # add(4, 4)
    # print(f'add count called: {add.counter}')

    count = Calculate(10)
    count.add(3)
    count.add(4)
    count.add(1)
    count.add.__wrapped__(count, 4)
    print(f'add count called: {Calculate.add.counter}')

    def sub(self, y):
        self.x = self.x - y

    new_sub = sub.__get__(count, Calculate)
    print(count.x)
    new_sub(5)
    print(count.x)