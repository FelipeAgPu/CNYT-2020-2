import unittest
import complex


class TestComplex(unittest.TestCase):

    def test_add(self):
        result = complex.add([5, 2], [3, 1])
        self.assertEqual(result, [8, 3])

    def test_subs(self):
        result = complex.subs([5, 2], [3, 1])
        self.assertEqual(result, [2, 1])

    def test_mult(self):
        result = complex.mult([5, 2], [3, 1])
        self.assertEqual(result, [13, 11])

    def test_divi(self):
        result = complex.divi([5, 2], [3, 1])
        self.assertEqual(result, [1.7, 0.1])

    def test_mod(self):
        result = complex.mod([3, 4])
        self.assertEqual(result, 5.0)

    def test_conj(self):
        result = complex.conj([-5, 2])
        self.assertEqual(result, [-5, -2])

    def test_conv(self):
        result = complex.coor_to_polar([-5, 2])
        self.assertEqual(result, [5.385, -0.381])

    def test_phase(self):
        result = complex.phase([-5, 2])
        self.assertEqual(result, -0.381)
        