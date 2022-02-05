import math
from math import sqrt


def solver1(a, b):
    if a == 0:
        text = "Коэффициент при x не может быть равен 0."
        return text
    x = -b / a
    text = "X: %s" % x
    return text


def solver2(a, b, c):
    if a == 0:
        text = "Коэффициент при x в степени 2 не может быть равен 0."
        return text
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        text = "X1: %s \n X2: %s \n" % (x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        text = "X: %s \n" % x
    else:
        text = "У этого уравнения два комплексных корня."
        z1 = complex(-b + sqrt(abs(b ** 2 - 4 * a * c)) / (2 * a))
        z2 = complex(-b - sqrt(abs(b ** 2 - 4 * a * c)) / (2 * a))
        text_1 = "Z1: %s \n Z2: %s \n" % (z1, z2)
        return text, text_1