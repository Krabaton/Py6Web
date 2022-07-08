import time
from functools import wraps


def wrong_timelogger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


def timelogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@timelogger
def long_loop(n: int) -> None:
    """
    Long loop
    :param n:
    :return: None
    """
    while n > 0:
        n -= 1


if __name__ == '__main__':
    long_loop(100000)
    print(f'Name: {long_loop.__name__}')
    print(f'Docstring: {long_loop.__doc__}')
    print(f'Annotation: {long_loop.__annotations__}')
