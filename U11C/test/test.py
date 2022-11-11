import os, sys
import unittest
sys.path.append('')
import src.calculadora as calculadora

# Imports para configurar docs_from_tests

from pathlib import Path
from docs_from_tests.instrument_call_hierarchy import (
    instrument_and_import_package,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)

instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), '..', 'calculadora'), 'calculadora')

class MyTest(unittest.TestCase):
    def test_hello_world(self):

        # Inicio de la secuencia
        initialise_call_hierarchy('start')

        valid_result = calculadora.sumar(1, 2)
        self.assertEqual(valid_result, 3)

        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__)
                                                , '..'
                                                , 'doc'
                                                , 'diagrama de secuencia.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

if __name__ == '__main__':
    unittest.main()
