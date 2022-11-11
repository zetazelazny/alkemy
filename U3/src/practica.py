import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logHandler = logging.FileHandler('practica.log')

logFormat = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

logHandler.setFormatter(logFormat)

logger.addHandler(logHandler)


fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]

for x in fruits:
    try:
        x_lower = x.lower()
        message = ('Conversion exitosa: {x} --> {x_lower}').format(x = x, x_lower = x_lower)
        logger.info(message)
    except:
        message = ('Conversion fallida: {x}').format(x = x)
        logger.error(message)
