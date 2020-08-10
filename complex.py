# Autor: Juan Felipe Aguas Pulido
import math


def add(c1, c2):
    """
    Adds two complex numbers
    :list c1: List of two items, first one the real part and second one the imaginary part
    :list c2: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = [c1[0] + c2[0], c1[1] + c2[1]]
    return ans


def subs(c1, c2):
    """
    Substracts two complex numbers
    :list c1: List of two items, first one the real part and second one the imaginary part
    :list c2: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = [c1[0] - c2[0], c1[1] - c2[1]]
    return ans


def mult(c1, c2):
    """
    Multiplies two complex numbers
    :list c1: List of two items, first one the real part and second one the imaginary part
    :list c2: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = [round(c1[0]*c2[0] - c1[1]*c2[1], 3), round(c1[0]*c2[1] + c1[1]*c2[0], 3)]
    return ans


def divi(c1, c2):
    """
    Divides two complex numbers
    :list c1: List of two items, first one the real part and second one the imaginary part
    :list c2: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    den = c2[0] ** 2 + c2[1] ** 2
    ans = [round((c1[0] * c2[0] + c1[1] * c2[1]) / den, 3), round((c2[0] * c1[1] - c1[0] * c2[1]) / den, 3)]
    return ans


def mod(c):
    """
    Returns the module of a complex number
    :list c: List of two items, first one the real part and second one the imaginary part
    :return float:
    """
    ans = (c[0] ** 2 + c[1] ** 2) ** 0.5
    return round(ans, 3)


def conj(c):
    """
    Returns the conjugated of a complex number
    :list c: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = [c[0], c[1] * -1]
    return ans


def coor_to_polar(c):
    """
    Changes a complex number from Cartesian to Polar coordinates
    :list c: List of two items
    :return list:
    """
    p = mod(c)
    theta = math.atan(c[1] / c[0])
    ans = [round(p, 3), round(theta, 3)]
    return ans


def polar_to_coor(c):
    """
    Changes a complex number from Polar to Cartesian coordinates
    :list c: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = [round(c[0] * math.cos(c[1]), 3), round(c[0] * math.sin(c[1]), 3)]
    return ans


def phase(c):
    """
    Returns the phase of a complex number
    :list c: List of two items, first one the real part and second one the imaginary part
    :return list:
    """
    ans = math.atan(c[1] / c[0])
    return round(ans, 3)


print(polar_to_coor([5, 3.15]))