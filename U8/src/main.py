# Imports
import logging
import logging.config

# Logger configuration
logger = logging.config.fileConfig(fname='/src/log_config.conf',
                                   disable_existing_loggers=False)
logger = logging.getLogger('mainLogger')


def words_size(lista_palabras):
    """
    Calculate the size for each element in a given list
    :param lista_palabras: List containing words
    :returns: List containing word size in the same order as the parameter list
    """
    logger.info(('Valores de lista: {x}').format(x=lista_palabras))
    lista_size_palabras = []
    for palabra in lista_palabras:
        longitud_palabra = len(palabra)
        logger.info(('Palabra: {p}').format(p=palabra))
        logger.info(('Longitud: {l}').format(l=longitud_palabra))
        lista_size_palabras.append(longitud_palabra)
    return lista_size_palabras


if __name__ == '__main__':
    print(words_size.__doc__)
    lista_inicial = ['perro', 'elefante', 'dragón']
    logger.info('Llamando a funcion words_size()')
    lista_retorno = words_size(lista_inicial)
    logger.info(('Valores recibidos: {l}').format(l=lista_retorno))
