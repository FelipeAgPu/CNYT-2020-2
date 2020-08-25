# Autor Juan Felipe Aguas Pulido

import unittest
import vectors_matrices as vec_mat


class TestVectorsMatrices(unittest.TestCase):

    def test_add(self):
        # Test 1
        result = vec_mat.add([[1, 2], [0, 0], [5, -7]], [[3, 4], [-6, 0], [7, 7]])
        self.assertEqual(result, [[4, 6], [-6, 0], [12, 0]])
        # Test 2
        result = vec_mat.add([[10, 0], [2, 0]], [[-10, 2], [-4, 4]])
        self.assertEqual(result, [[0, 2], [-2, 4]])
        # Test 3
        result = vec_mat.add([[9, 3], [3, -1], [-8, -3]], [[0, 0], [-6, 10], [5, 6]])
        self.assertEqual(result, [[9, 3], [-3, 9], [-3, 3]])

    def test_subs(self):
        # Test 1
        result = vec_mat.subs([[1, 2], [0, 0], [5, -7]], [[3, 4], [-6, 0], [7, 7]])
        self.assertEqual(result, [[-2, -2], [6, 0], [-2, -14]])
        # Test 2
        result = vec_mat.subs([[10, 0], [2, 0]], [[-10, 2], [-4, 4]])
        self.assertEqual(result, [[20, -2], [6, -4]])
        # Test 3
        result = vec_mat.subs([[9, 3], [3, -1], [-8, -3]], [[0, 0], [-6, 10], [5, 6]])
        self.assertEqual(result, [[9, 3], [9, -11], [-13, -9]])

    def test_additiveinv(self):
        # Test 1
        result = vec_mat.additive_inverse([[1, 7], [2, -56]])
        self.assertEqual(result, [[-1, -7], [-2, 56]])
        # Test 2
        result = vec_mat.additive_inverse([[0, 0], [0, 0], [0, 0]])
        self.assertEqual(result, [[0, 0], [0, 0], [0, 0]])
        # Test 3
        result = vec_mat.additive_inverse([[10, 5], [-4, 3], [-5, -5]])
        self.assertEqual(result, [[-10, -5], [4, -3], [5, 5]])

    def test_multesc(self):
        # Test 1
        result = vec_mat.mult_escalar([-1, 0], [[5, 0], [3, -1], [1, 1]])
        self.assertEqual(result, [[-5, 0], [-3, 1], [-1, -1]])
        # Test 2
        result = vec_mat.mult_escalar([5, 2], [[3, -5], [0, 0], [7, 6]])
        self.assertEqual(result, [[25, -19], [0, 0], [23, 44]])
        # Test 3
        result = vec_mat.mult_escalar([6, -5], [[23, 6], [-1, 7], [8, -4]])
        self.assertEqual(result, [[168, -79], [29, 47], [28, -64]])

    def test_addm(self):
        # Test 1
        result = vec_mat.add_mat([[[2, 4], [5, 2.3], [3, 6]], [[7.7, 4], [6, 9], [1, 0]], [[-4, -2], [0, 0], [0, -1]]],
                                 [[[9, 1], [0, -2.8], [-4, 12]], [[10, -2], [1, 1], [-5, -5]], [[6, -7], [9, 6.9], [1, 3]]]
                                 )
        self.assertEqual(result, [[[11, 5], [5, -0.5], [-1, 18]], [[17.7, 2], [7, 10], [-4, -5]], [[2, -9], [9, 6.9], [1, 2]]])
        # Test 2
        result = vec_mat.add_mat([[[3, 4],[7, -9]], [[2, 2], [0, -3]]], [[[2, 1], [4, 5]], [[7,7], [8, 0]]])
        self.assertEqual(result, [[[5, 5], [11, -4]], [[9, 9], [8, -3]]])
        # Test 3
        result = vec_mat.add_mat([[[2, 1], [-7, 3], [6, 7]], [[3, 2], [8, 2], [7, 5]]], [[[-5, 4], [0, 5], [-7, 1]], [[5, 3], [2, 8], [5, -6]]])
        self.assertEqual(result, [[[-3, 5], [-7, 8], [-1, 8]], [[8, 5], [10, 10], [12, -1]]])

    def test_additiveinvm(self):
        # Test 1
        result = vec_mat.additive_inverse_mat([[[2, 4], [5, 2], [3, 6]], [[7, 4], [6, 9], [1, 0]], [[-4, -2], [0, 0], [0, -1]]])
        self.assertEqual(result, [[[-2, -4], [-5, -2], [-3, -6]], [[-7, -4], [-6, -9], [-1, 0]], [[4, 2], [0, 0], [0, 1]]])
        # Test 2
        result = vec_mat.additive_inverse_mat([[[3, 4],[7, -9]], [[2, 2], [0, -3]]])
        self.assertEqual(result, [[[-3, -4],[-7, 9]], [[-2, -2], [0, 3]]])
        # Test 3
        result = vec_mat.additive_inverse_mat([[[2, 1], [-7, 3], [6, 7]], [[3, 2], [8, 2], [7, 5]]])
        self.assertEqual(result, [[[-2, -1], [7, -3], [-6, -7]], [[-3, -2], [-8, -2], [-7, -5]]])

    def test_multescm(self):
        # Test 1
        result = vec_mat.mult_escalar_mat([3, -1], [[[2, 5], [1, 3]], [[7, 4], [3, 2]], [[1, 0], [4, 5]]])
        self.assertEqual(result,[[[11, 13], [6, 8]], [[25, 5], [11, 3]], [[3, -1], [17, 11]]])
        # Test 2
        result = vec_mat.mult_escalar_mat([6, 2], [[[-4, 5], [1, 3]], [[6, -7], [-8, 9]]])
        self.assertEqual(result, [[[-34, 22], [0, 20]], [[50, -30], [-66, 38]]])
        # Test 3
        result = vec_mat.mult_escalar_mat([-1, 0], [[[2, 0], [5, 4]], [[4, 5], [3, 5]]])
        self.assertEqual(result, [[[-2, 0], [-5, -4]], [[-4, -5], [-3, -5]]])

    def test_tranpose(self):
        # Test 1
        result = vec_mat.transpose([[[4, 1], [4, 2]]])
        self.assertEqual(result, [[[4, 1]], [[4, 2]]])
        # Test 2
        result = vec_mat.transpose([[[1, 0], [3, 4], [1, 4]], [[2, 0], [4, 5], [3, 2]]])
        self.assertEqual(result, [[[1, 0], [2, 0]], [[3, 4], [4, 5]], [[1, 4], [3, 2]]])
        # Test 3
        result = vec_mat.transpose([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(result, [[1,3,5], [2, 4, 6]])

    def test_conjugated(self):
        # Test 1
        result = vec_mat.conjugated([[[2, 5], [1, 0]], [[1, 4], [3, 2]], [[2, 3], [4, 5]]])
        self.assertEqual(result, [[[2, -5], [1, 0]], [[1, -4], [3, -2]], [[2, -3], [4, -5]]])
        # Test 2
        result = vec_mat.conjugated([[[-10, 1], [0, 1], [7, 9]], [[-8, -2], [3, 2], [7, -1]]])
        self.assertEqual(result, [[[-10, -1], [0, -1], [7, -9]], [[-8, 2], [3, -2], [7, 1]]])
        # Test 3
        result = vec_mat.conjugated([[[1, -5], [3, 5]], [[9, -4], [-4, 6]], [[8, -4], [3, -2]]])
        self.assertEqual(result, [[[1, 5], [3, -5]], [[9, 4], [-4, -6]], [[8, 4], [3, 2]]])

    def test_adjoint(self):
        # Test 1
        result = vec_mat.adjoint([[[2, 5], [1, 0]], [[1, 4], [3, 2]], [[2, 3], [4, 5]]])
        self.assertEqual(result, [[[2, -5], [1, -4], [2, -3]], [[1, 0], [3, -2], [4, -5]]])
        # Test 2
        result = vec_mat.adjoint([[[0,1], [4, 2]]])
        self.assertEqual(result, [[[0, -1]], [[4, -2]]])
        # Test 3
        result = vec_mat.adjoint([[[5, 7], [6, 0]], [[0, 0], [4, 5]], [[3, 7], [0, 2]]])
        self.assertEqual(result, [[[5, -7], [0, 0], [3, -7]], [[6, 0], [4, -5], [0, -2]]])

    def test_multm(self):
        # Test 1
        result = vec_mat.mult_mat([[[1, 3], [5, 2], [-3, 4]], [[0, 9], [8, 3], [2, -5]], [[1, 0], [3, 4], [6, 7]]],
                                  [[[2, 6], [1, -4]], [[6, -3], [7, 2]]]
                                  )
        self.assertEqual(result, 'Not possible')
        # Test 2
        result = vec_mat.mult_mat([[[1, 0], [2, 0]], [[3, 4], [4, 5]]], [[[4, 5], [1, 3]], [[6, 7], [8, 9]]])
        self.assertEqual(result, [[[16, 19], [17, 21]], [[-19, 89], [-22, 89]]])
        # Test 3
        result = vec_mat.mult_mat([[[1, 0], [0, 0]], [[0, 0], [1, 0]]], [[[3, 3], [0, -5]], [[2, -9], [9, 6]]])
        self.assertEqual(result, [[[3, 3], [0, -5]], [[2, -9], [9, 6]]])

    def test_action(self):
        # Test 1
        result = vec_mat.action([[[3, 3], [0, -5]], [[2, -9], [9, 6]]], [[1, 1],[3, 5], [2, 2]])
        self.assertEqual(result, 'Not possible')
        # Test 2
        result = vec_mat.action([[[3, 3], [0, -5]], [[2, -9], [9, 6]]], [[[1, 1]],[[3, 5]]])
        self.assertEqual(result, [[[25, -9]], [[8, 56]]])
        # Test 3
        result = vec_mat.action([[[1, 0], [2, 0]], [[3, 4], [4, 5]]], [[[4, 5]], [[1, 3]]])
        self.assertEqual(result, [[[6, 11]], [[-19, 48]]])

    def test_dot(self):
        # Test 1
        result = vec_mat.dot_product([[0, 0], [0, 0], [0, 0]], [[2, 3], [5, 6], [-7, 8]])
        self.assertEqual(result, [0, 0])
        # Test 2
        result = vec_mat.dot_product([[1, 2], [0, 0], [5, -7]], [[2, 3], [5, 6], [-7, 8]])
        self.assertEqual(result, [17, 96])
        # Test 3
        result = vec_mat.dot_product([[9, 3], [3, -1], [-8, -3]], [[3, 4], [-6, 0], [7, 7]])
        self.assertEqual(result, [-38, -26])

    def test_norm(self):
        # Test 1
        result = vec_mat.vector_norm([[1, 0], [2, 0]])
        self.assertEqual(result, 2.24)
        # Test 2
        result = vec_mat.vector_norm([[4, 5], [1, 3], [29, 54], [31, 66]])
        self.assertEqual(result, 95.52)
        # Test 3
        result = vec_mat.vector_norm([[5, 1], [4, 2], [6, 3], [1, 7]])
        self.assertEqual(result, 11.87)

    def test_dist(self):
        # Test 1
        result = vec_mat.vectors_distance([[3, 0], [1, 0], [2, 0]], [[2, 0], [2, 0], [-1, 0]])
        self.assertEqual(result, 3.32)
        # Test 2
        result = vec_mat.vectors_distance([[3, 1], [2, 6], [7, 5], [3, 6]], [[5, 1], [4, 2], [6, 3], [1, 7]])
        self.assertEqual(result, 5.83)

    def test_unit(self):
        # Test 1
        result = vec_mat.is_unitary([[[1, 0], [0, 0], [0, 0]], [[0, 0], [1, 0], [0, 0]], [[0, 0], [0, 0], [1, 0]]])
        self.assertEqual(result, True)
        # Test 2
        result = vec_mat.is_unitary([[[0, 2], [0, 1]], [[0, 4], [2, 0]]])
        self.assertEqual(result, False)

    def test_tensor(self):
        # Test 1
        result = vec_mat.tensor(
            [[[3, 2], [5, -1], [0, 2]], [[0, 0], [12, 0], [6, -3]], [[2, 0], [4, 4], [9, 3]]],
            [[[1, 0], [3, 4], [5, -7]], [[10, 2], [6, 0], [2, 5]], [[0, 0], [1, 0], [2, 9]]])
        self.assertEqual(result, [
            [[[[3, 2], [1, 18], [29, -11]], [[26, 26], [18, 12], [-4, 19]], [[0, 0], [3, 2], [-12, 31]]],
             [[[5, -1], [19, 17], [18, -40]], [[52, 0], [30, -6], [15, 23]], [[0, 0], [5, -1], [19, 43]]],
             [[[0, 2], [-8, 6], [14, 10]], [[-4, 20], [0, 12], [-10, 4]], [[0, 0], [0, 2], [-18, 4]]]],
            [[[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]],
             [[[12, 0], [36, 48], [60, -84]], [[120, 24], [72, 0], [24, 60]], [[0, 0], [12, 0], [24, 108]]],
             [[[6, -3], [30, 15], [9, -57]], [[66, -18], [36, -18], [27, 24]], [[0, 0], [6, -3], [39, 48]]]],
            [[[[2, 0], [6, 8], [10, -14]], [[20, 4], [12, 0], [4, 10]], [[0, 0], [2, 0], [4, 18]]],
             [[[4, 4], [-4, 28], [48, -8]], [[32, 48], [24, 24], [-12, 28]], [[0, 0], [4, 4], [-28, 44]]],
             [[[9, 3], [15, 45], [66, -48]], [[84, 48], [54, 18], [3, 51]], [[0, 0], [9, 3], [-9, 87]]]]]
                         )
