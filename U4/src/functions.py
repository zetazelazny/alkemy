import logging
import logging.config

logging.config.fileConfig(fname='.\src\log_config_file.conf', disable_existing_loggers=False)

logger = logging.getLogger('functionsLogger')

f = open('.\src\cuento.txt', 'r')
cantLineasF = f.readlines()
logger.info(('cuento.txt - Cantidad de renglones: {a}').format(a = cantLineasF))
numLinea = 0
for linea in f:
    cantPalabras = str(len(linea.split()))
    logger.info(('Renglon {numero}: {cantidad} palabras').format(numero=numLinea, cantidad=cantPalabras))
    numLinea+=1