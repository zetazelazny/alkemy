import logging
import logging.config

logger = logging.config.fileConfig(fname='.\src\log_config.conf', disable_existing_loggers=False)

logger = logging.getLogger('mainLogger')

def words_size (lista_palabras):
    logger.info(('Valores de lista: {x}').format(x = lista_palabras))
    lista_size_palabras = []
    for palabra in lista_palabras:
        longitud_palabra = len(palabra)
        logger.info(('Palabra: {p}').format(p = palabra))
        logger.info(('Longitud: {l}').format(l = longitud_palabra))
        lista_size_palabras.append(longitud_palabra)
    return lista_size_palabras


if __name__ == '__main__':
    lista_inicial = ['perro', 'elefante', 'dragón']
    logger.info('Llamando a funcion words_size()')
    lista_retorno = words_size(lista_inicial)
    logger.info(('Valores recibidos: {l}').format(l = lista_retorno))
    
