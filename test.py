#Autor Juan Felipe Aguas Pulido

import unittest
import complex


class TestComplex(unittest.TestCase):

    def test_add(self):
        # Test 1
        result = complex.add([5, 2], [3, 1])
        self.assertEqual(result, [8, 3])
        # Test 2
        result = complex.add([5, -3], [-4, 2])
        self.assertEqual(result, [1, -1])
        # Test 3
        result = complex.add([-6, 8], [-12, -9])
        self.assertEqual(result, [-18, -1])

    def test_subs(self):
        # Test 1
        result = complex.subs([5, 2], [3, 1])
        self.assertEqual(result, [2, 1])
        # Test 2
        result = complex.subs([3, 8], [0, -2])
        self.assertEqual(result, [3, 10])
        # Test 3
        result = complex.subs([6, -1], [-11, 13])
        self.assertEqual(result, [17, -14])

    def test_mult(self):
        # Test 1
        result = complex.mult([5, 2], [3, 1])
        self.assertEqual(result, [13, 11])
        # Test 2
        result = complex.mult([27, 12], [13, 1])
        self.assertEqual(result, [339, 183])
        # Test 3
        result = complex.mult([4, -3], [1, 10])
        self.assertEqual(result, [34, 37])

    def test_divi(self):
        # Test 1
        result = complex.divi([5, 2], [3, 1])
        self.assertEqual(result, [1.7, 0.1])
        # Test 2
        result = complex.divi([11, 12], [0, -7])
        self.assertEqual(result, [-1.714, 1.571])
        # Test 3
        result = complex.divi([8, 0], [-10, 4])
        self.assertEqual(result, [-0.690, -0.276])

    def test_mod(self):
        # Test 1
        result = complex.mod([3, 4])
        self.assertEqual(result, 5.0)
        # Test 2
        result = complex.mod([13, 3])
        self.assertEqual(result, 13.342)
        # Test 3
        result = complex.mod([-14, 0])
        self.assertEqual(result, 14)

    def test_conj(self):
        # Test 1
        result = complex.conj([-5, 2])
        self.assertEqual(result, [-5, -2])
        # Test 2
        result = complex.conj([4, 4])
        self.assertEqual(result, [4, -4])
        # Test 3
        result = complex.conj([0, -11])
        self.assertEqual(result, [0, 11])

    def test_conv(self):
        # Test 1
        result = complex.coor_to_polar([-5, 2])
        self.assertEqual(result, [5.385, -0.381])
        # Test 2
        result = complex.coor_to_polar([-5, 2])
        self.assertEqual(result, [5.385, -0.381])
        # Test 3

    def test_phase(self):
        # Test 1
        result = complex.phase([-5, 2])
        self.assertEqual(result, -0.381)
        # Test 2
        result = complex.phase([3, 4])
        self.assertEqual(result, 0.927)
        # Test 3
        result = complex.phase([7, -4])
        self.assertEqual(result, -0.519)

if __name__ == '__main__':
    unittest.main()