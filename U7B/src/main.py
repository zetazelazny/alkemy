from datetime import date, datetime

class Empleado:
    """
    Clase que contiene las propiedades de un empleado.

    :param nombre: Nombre del empleado
    :param apellido: Apellido del empleado
    :param fecha_nacimiento: Fecha de nacimiento del empleado
    :param nro_dni: Numero de documento del empleado

    """

    def __init__(self, nombre, apellido, fecha_nacimiento, nro_dni):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nro_dni = nro_dni

    def edad(self):
        """
        Esta funcion no recibe parametros

        :return: Edad del empleado
        :rtype: int
        """

        today = date.today()
        fec_nacimiento = datetime.strptime(self.fecha_nacimiento, '%Y-%m-%d')
        edad =today.year - fec_nacimiento.year - ((today.month, today.day) < (fec_nacimiento.month, fec_nacimiento.day))
        return edad

    def presentacion(self):
        """
        Esta funcion no recibe parametros

        :return: Nombre, apellido, fecha de nacimiento y numero de documento del empleado
        :rtype: String
        """
        return f"Hola, soy {self.nombre} {self.apellido}. Nací el {self.fecha_nacimiento} y ni DNI es {self.nro_dni}"

if __name__ == '__main__':
    empleado = Empleado('matias', 'zelazny', '1999-08-05', '42102578')
    print(empleado.edad())        
    print(empleado.presentacion())