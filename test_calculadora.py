import unittest

# Importamos la clase calculadora
from calculadora import Calculadora

class TestMyCalculator(unittest.TestCase):

    def test_initial_value(self):
        calc = Calculadora()
        self.assertEqual(0, calc.value)