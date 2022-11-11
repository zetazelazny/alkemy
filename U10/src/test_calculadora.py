import unittest
import calculadora


class TestMethods(unittest.TestCase):

    def test_sumar_dos_positivos(self):
        self.assertEqual(calculadora.sumar(1, 2), 3)

    def test_sumar_positivo_negativo(self):
        self.assertEqual(calculadora.sumar(1, -3), -2)

    def test_sumar_dos_negativos(self):
        self.assertEqual(calculadora.sumar(-9, -8), -17)

    def test_restas_dos_positivos(self):
        self.assertEqual(calculadora.restar(2, 1), 1)

    def test_restar_positivo_negativo(self):
        self.assertEqual(calculadora.restar(1, -3), 4)

    def test_restar_dos_negativos(self):
        self.assertEqual(calculadora.restar(-9, -8), -1)

    def test_multiplicar_dos_positivos(self):
        self.assertEqual(calculadora.multiplicar(2, 1), 2)

    def test_multiplicar_positivo_negativo(self):
        self.assertEqual(calculadora.multiplicar(1, -3), -3)

    def test_multiplicar_dos_negativos(self):
        self.assertEqual(calculadora.multiplicar(-9, -2), 18)

    def test_dividir_dos_positivos(self):
        self.assertEqual(calculadora.dividir(2, 1), 2)

    def test_dividir_positivo_negativo(self):
        self.assertEqual(calculadora.dividir(10, -5), -2)

    def test_dividir_dos_negativos(self):
        self.assertEqual(calculadora.dividir(-10, -2), 5)


if __name__ == '__main__':
    unittest.main()
