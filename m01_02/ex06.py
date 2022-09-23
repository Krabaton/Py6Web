from functools import wraps
import logging


def logged(level, name=None, message=None):
    def decorate(func):
        log_name = name if name else func.__module__
        log_message = message if message else func.__name__
        logger = logging.getLogger(log_name)
        logging.basicConfig(level=logging.DEBUG)

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logger.log(level, log_message)
            return result

        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.ERROR, 'greeting')
def prefix_name(name):
    return f'Mr.(s) {name}'


if __name__ == '__main__':

    print(add(2, 3))
    print(prefix_name('Andrij'))
