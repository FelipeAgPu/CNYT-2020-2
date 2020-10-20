import complex
import vectors_matrices as vm
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# Función auxiliar
def action(m1, v1):
    if len(m1[0]) == len(v1):
        m = [[0 for i in range(len(v1[0]))] for j in range(len(m1))]
        for row in range(len(m1)):
            for column in range(len(v1[0])):
                for aux in range(len(m1[0])):
                    m[row][column] = round(m[row][column] + (m1[row][aux] * v1[aux][column]), 3)
        return m


# Punto 1
def clicks_boolean(matrix, vector, t):
    """
    Function that calculates the marbles experiment
    :param matrix:Array of n*m items, each item is boolean
    :param vector:Array of m items, each item is a real number
    :param t:Integer
    :return Array:
    """
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    ans = vector
    for i in range(t):
        ans = action(matrix, ans)
    return ans


# Punto 2
def clicks_prob(matrix, vector, t):
    """
    Function that calculates the probabilities of a probabilistic system in t clicks
    :param matrix:Array of n*m items, each item is a real number
    :param vector:Array of m items, each item is a real number
    :param t:Integer
    :return List:
    """
    ans = vector
    for i in range(t):
        ans = action(matrix, ans)
    return ans


# Punto 3
def clicks_cuant(matrix, vector, t):
    """
    Function that calculates t clicks in a quantum system
    :param matrix: Array of n*m items, each item is a complex number
    :param vector: Array of m items, each item is a complex number
    :param t: Integer
    :return Array:
    """
    ans = vector
    for i in range(t):
        ans = vm.action(matrix, ans)
    for i in range(len(ans)):
        ans[i][0] = round(complex.mod(ans[i][0]) ** 2, 3)
    return ans


#Punto 4
def plot(probs):
    """
    Function that plots the probabilities of a status vector
    :param probs: List
    """
    estados = [x for x in range(len(probs))]
    fig, ax = plt.subplots()
    ax.set_ylabel('Probabilidades')
    ax.set_xlabel('Estados')
    ax.set_title('Sistema Cuantico')
    plt.bar(estados, probs)
    plt.savefig('probabilities.png')
    plt.show()
