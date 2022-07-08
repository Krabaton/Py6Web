import logging

from my_logger import get_logger

logger = get_logger(__name__)


def test():
    baz = 10
    logger.info(f'Start test')
    logger.debug(f'baz={baz}')


def foo():
    logger.warning('Badabum')


if __name__ == '__main__':
    test()
    foo()
    logger.log(logging.DEBUG, 'End script')
