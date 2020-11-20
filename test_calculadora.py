import unittest
from calculadora import Calculadora


class TestMyCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)