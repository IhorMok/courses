#logging

import logging
from div import d
# # logging.basicConfig(level = logging.INFO)
# logger = logging.getLogger(__name__)
# logger.info('info')
# logger.debug('debug')
# logger.warning('Warning')
# # logger.error('error')

fmt = '%(asctime)s:%(name)s:%(levelname)s - %(message)s'
logging.basicConfig(filename = 'log.log',filemode = 'w',
                     level = logging.DEBUG, format=fmt)

# logging.debug('msg')
logging.debug('started function d')
print(d(67, 97))
logging.debug('done')

# import logging
#
#
#
# def d(a, b):
#     logging.debug('stared function d')
#     try:
#         c = a/b
#         logging.debug(f'd return {c}')
#         return c
#     except ArithmeticError as e:
#         logging.exception('b is zero', exc_info=True)
#         logging.error(f'{e}')

