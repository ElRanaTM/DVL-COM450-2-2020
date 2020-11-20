import unittest
from calculadora import Calculadora


class TestMyCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    def test_add_method(self):
        self.calc.add(1, 3)
        self.assertEqual(4, self.calc.value)

    def test_sub_method(self):
        self.calc.sub(5, 3)
        self.assertEqual(2, self.calc.value)

    def test_mul_method(self):
        self.calc.mul(2, 6)
        self.assertEqual(12, self.calc.value)

    def test_div_method(self):
        self.calc.div(10, 5)
        self.assertEqual(2, self.calc.value)