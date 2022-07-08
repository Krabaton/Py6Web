import logging

logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(funcName)-15s %(message)s')
logging.info('Start')


def test():
    baz = 10
    logging.debug(f'baz={baz}')


test()