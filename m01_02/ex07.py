from functools import wraps, partial
import logging


def logged(func=None, *_, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    log_name = name if name else func.__module__
    log_message = message if message else func.__name__
    logger = logging.getLogger(log_name)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(level, log_message)
        return result

    return wrapper


@logged
def add(x, y):
    return x + y


@logged()
def sub(x, y):
    return x - y


@logged(level=logging.CRITICAL, name='greeting')
def prefix_name(name):
    return f'Mr.(s) {name}'


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(add(2, 3))
    print(sub(3, 2))
    print(prefix_name('Andrij'))
