def search_by_index():
    medios_transporte = ['auto', 'avion', 'barco', 'bicicleta', 'omnibus']
    try:
        index = int(input('Ingrese una posicion: '))
        print(medios_transporte[index])
    except IndexError:
        print('No existe el indice ingresado')
        search_by_index()
    except ValueError:
        print('Ingrese un indice numerico')
        search_by_index()


if __name__ == '__main__':
    search_by_index()
