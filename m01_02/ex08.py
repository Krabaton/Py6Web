from functools import wraps, partial
from inspect import signature
import logging


def optional_logger(func):
    logger = logging.getLogger(func.__name__)
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        result = func(*args, **kwargs)
        if debug:
            logger.log(logging.DEBUG, f'Signature: {signature(func)}. Arguments: {args} {kwargs}')
        return result
    return wrapper


@optional_logger
def prefix_name(name):
    return f'Mr.(s) {name}'


if __name__ == '__main__':

    print(prefix_name('Andrij'))
    print(prefix_name('Volodymyr', debug=True))
