
import logging


logger = logging.getLogger('div')
def d(a, b):
    logger.debug('stared function d')
    try:
        c = a*b
        logger.debug(f'd return {c}')
        return c
    except ArithmeticError as e:
        logger.exception('b is zero', exc_info=True)
        logger.error(f'{e}')
