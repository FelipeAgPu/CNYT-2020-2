# Autor: Juan Felipe Aguas Pulido
import math

def add(c1, c2):
    """
    :list c1: List of two items, first one the real part and second one the imaginary part
    :list c2: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = [c1[0] + c2[0], c1[1] + c2[1]]
    return ans


def subs(c1, c2):
    """
    :list c1: List of two items, first one the real part and second one the imaginary part
    :list c2: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = [c1[0] - c2[0], c1[1] - c2[1]]
    return ans


def mult(c1, c2):
    """
    :list c1: List of two items, first one the real part and second one the imaginary part
    :list c2: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = [c1[0]*c2[0] - c1[1]*c2[1], c1[0]*c2[1] + c1[1]*c2[0]]
    return ans


def divi(c1, c2):
    """
    :list c1: List of two items, first one the real part and second one the imaginary part
    :list c2: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    den = c2[0] ** 2 + c2[1] ** 2
    ans = [(c1[0] * c2[0] + c1[1] * c2[1]) / den, (c2[0] * c1[1] - c1[0] * c2[1]) / den]
    return ans


def mod(c):
    """
    :list c: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = (c[0] ** 2 + c[1] ** 2)** 0.5
    return ans


def conj(c):
    """
    :list c: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = [c[0], c[1] * -1]
    return ans


def coorToPolar(c):
    """
    :list c: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    p = mod(c)
    theta = math.atan(c[1] / c[0])
    ans = [p, theta]
    return ans


def phase(c):
    """
    :list c: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = math.atan(c[1] / c[0])
    return ans
