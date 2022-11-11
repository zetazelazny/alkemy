import logging
import logging.config

logging.config.fileConfig(fname='.\src\log_config_file.conf', disable_existing_loggers=False)

logger = logging.getLogger('mainLogger')

try:
    f = open('.\src\cuento.txt', 'r')
    logger.info('...Leyendo el archivo...')
    f.read()
    logger.info('...Archivo procesado...')
except:
    logger.error('No se pudo abrir el archivo')