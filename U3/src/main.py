import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

w_handler = logging.StreamHandler()
e_handler = logging.FileHandler('main.log')

w_handler.setLevel(logging.WARNING)
e_handler.setLevel(logging.ERROR)

w_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
e_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

w_handler.setFormatter(w_format)
e_handler.setFormatter(e_format)

logger.addHandler(w_handler)
logger.addHandler(e_handler)

logger.warning('Esto es un warning')
logger.error('Esto es un error')

