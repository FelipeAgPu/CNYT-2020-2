# Autor Juan Felipe Aguas Pulido
import complex


def add(v1, v2):
    """
    Adds two complex vectors
    :Array c1: Array of n items, each item is a complex number
    :Array c2: Array of n items, each item is a complex number
    :return Array:
    """
    ans_vector = []
    for i in range(len(v1)):
        ans_vector.append(complex.add(v1[i], v2[i]))
    return ans_vector


# Auxiliar function
def subs(v1, v2):
    """
    Substracts two complex vectors
    :Array c1: Array of n items, each item is a complex number
    :Array c2: Array of n items, each item is a complex number
    :return Array:
    """
    ans_vector = []
    for i in range(len(v1)):
        ans_vector.append(complex.subs(v1[i], v2[i]))
    return ans_vector


def additive_inverse(v):
    """
    Returns the additive inverse of a vector
    :Array v: Array of n items, each item is a complex number
    :return Array:
    """
    ans_vector = []
    for i in range(len(v)):
        ans_vector.append(complex.mult(v[i], [-1, 0]))
    return ans_vector


def mult_escalar(c, v):
    """
    Multiplies a scalar number by a complex vector
    :List c: List of two items, first one the real part and second one the imaginary part
    :Array v: Array of n items, each item is a complex number
    :return Array:
    """
    ans_vector = []
    for i in range(len(v)):
        ans_vector.append(complex.mult(c, v[i]))
    return ans_vector


def add_mat(m1, m2):
    """
    Adds two complex matrices
    :Array m1: Matrix of n*m dimentions, each item is a complex number
    :Array m2: Matrix of n*m dimentions, each item is a complex number
    :return Array:
    """
    ans = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(complex.add(m1[i][j], m2[i][j]))
        ans.append(row)
    return ans


def additive_inverse_mat(m):
    """
    Returns the additive inverse of a complex matrix
    :Array v: Matrix of n*m items, each item is a complex number
    :return Array:
    """
    ans = []
    for i in range(len(m)):
        ans.append([])
        for j in range(len(m[i])):
            ans[i].append(complex.mult(m[i][j], [-1, 0]))
    return ans


def mult_escalar_mat(c, m):
    """
    Multiplies a scalar number by a complex matrix
    :List c: List of two items, first one the real part and second one the imaginary part
    :Array m: Array of n*m items, each item is a complex number
    :return Array:
    """
    ans_vector = []
    for i in range(len(m)):
        ans_vector.append([])
        for j in range(len(m[i])):
            ans_vector[i].append(complex.mult(c, m[i][j]))
    return ans_vector


def transpose(matrix):
    """
    Returns the transpose of a matrix
    :Array matrix: Array of n*m items
    :return:
    """
    ans = []
    for i in range(len(matrix[0])):
        fila = []
        for j in range(len(matrix)):
            fila += [matrix[j][i]]
        ans += [fila]
    return ans


def conjugated(matrix):
    """
    Returns the conjugated of a matrix
    :Array matrix: Array of n*m items, each item is a complex number
    :return Array:
    """
    ans = matrix[::]
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            casilla = ans[i][j]
            casilla[1] *= -1
    return ans


def adjoint(matrix):
    """
    Returns the adjoint of a matrix
    :Array matrix: Array of n*m items, each item is a complex number
    :return Array:
    """
    ans = matrix[::]
    return transpose(conjugated(ans))


def mult_mat(m1, m2):
    """
    Function that multiplies two matrices
    :Array m1: Array of n*m items, each item is a complex number
    :Array m2: Array of n*m items, each item is a complex number
    :return Array:
    """
    if len(m1[0]) == len(m2):
        ans = [[[0, 0] for j in range(len(m2[0]))] for i in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    ans[i][j] = complex.add(ans[i][j], complex.mult(m1[i][k], m2[k][j]))
        return ans
    else:
        return 'Not possible'


def action(m, v):
    """
    Function that multiplies a matrix by a vector
    :Array m: Array of n*m items, each item is a complex number
    :Array v: Array of n items, each item is a complex number
    :return Array:
    """
    return mult_mat(m, v)


def dot_product(v1, v2):
    """
    Function that returns the dot product between two vectors
    :Array v1: Array of n items, each item is a complex number
    :Array v2: Array of n items, each item is a complex number
    :return Array:
    """
    if len(v1) == len(v2):
        ans = [0, 0]
        for i in range(len(v1)):
            ans = complex.add(ans, complex.mult(v1[i], v2[i]))
        return ans
    else:
        return 'Not possible'


def vector_norm(v):
    """
    Function that returns the norm of a vector
    :Array v: Array of n items, each item is a complex number
    :return Float:
    """
    addi = 0
    for i in range(len(v)):
        addi += (complex.mod(v[i]) ** 2)
    return round(addi ** 0.5, 2)


def vectors_distance(v1, v2):
    """
    Function that returns the distance between two vectors
    :Array v1: Array of n items, each item is a complex number
    :Array v2: Array of n items, each item is a complex number
    :return Array:
    """
    aux = subs(v1, v2)
    return vector_norm(aux)


def is_unitary(matrix):
    """
    Function that verifies if a matrix is unitary
    :Array matrix: Array of n*m items, each item is a complex number
    :return Array:
    """
    if len(matrix) == len(matrix[0]):
        id = [[[0, 0] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j:
                    id[i][j] = [1, 0]
        aux = adjoint(matrix)
        product = mult_mat(aux, matrix)
        ans = True
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if product[i][j] != id[i][j]:
                    ans = False
        if ans:
            return True
        else:
            return False
    else:
        return False


def is_herm(matrix):
    """
    Function that verifies if a matrix is hermitian
    :Array matrix: Array of n*m items, each item is a complex number
    :return Array:
    """
    ad = matrix[::]
    ad = adjoint(ad)
    ans = True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == ad[i][j] and matrix[i][j] == ad[i][j]:
                continue
            else:
                ans = False
    return ans


def tensor(m1, m2):
    """
    Function that does the tensor product between two matrices
    :Array m1: Array of n*m items, each item is a complex number
    :Array m2: Array of n*m items, each item is a complex number
    :return Array:
    """
    ans = [[0 for j in range(len(m1[0]))] for i in range(len(m1))]
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            ans[i][j] = mult_escalar_mat(m1[i][j], m2)
    return ans



