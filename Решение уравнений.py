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
        return text
    elif D == 0:
        x = -b / (2 * a)
        text = "X: %s \n" % x
        return text
    else:
        text = "У этого уравнения два комплексных корня."
        z1 = complex(-b + sqrt(abs(b ** 2 - 4 * a * c)) / (2 * a))
        z2 = complex(-b - sqrt(abs(b ** 2 - 4 * a * c)) / (2 * a))
        text_1 = "Z1: %s \n Z2: %s \n" % (z1, z2)
        return text_1


def solver3(a, b, c, d):
    if a == 0:
        return 'Коэффициент при x в степени 3 не может быть равен 0.'

    def sign(x):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1

    a /= d
    b /= d
    c /= d
    q = (a ** 2 - 3 * b) / 9
    r = (a * (2 * a ** 2 - 9 * b) + 27 * c) / 54
    r2 = r ** 2
    q3 = q ** 3
    if r2 < q3:
        t = math.acos(r / sqrt(q3)) / 3
        q = -2 * sqrt(q)
        x_0 = q * math.cos(t) - a / 3
        x_1 = q * math.cos(t + 2*math.pi / 3) - a / 3
        x_2 = q * math.cos(t - 2*math.pi / 3) - a / 3
        text = 'X1 = %s\n X2 = %s\n X3 = %s\n' % (x_0, x_1, x_2)
        return text
    elif r2 > q3:
        if q > 0:
            t = math.acosh(abs(r) / sqrt(q ** 3)) / 3
            x_0 = -2 * sign(r) * sqrt(q) * math.cosh(t) - a / 3
            x_1 = complex(sign(r) * sqrt(q) * math.cosh(t) - a / 3, sqrt(3) * sqrt(q) * math.sinh(t))
            x_2 = complex(sign(r) * sqrt(q) * math.cosh(t) - a / 3, -sqrt(3) * sqrt(q) * math.sinh(t))
            text = 'X1 = %s\n X2 = %s\n X3 = %s\n' % (x_0, x_1, x_2)
            return text
        else:
            t = math.asinh(abs(r) / sqrt(abs(q) ** 3)) / 3
            x_0 = -2 * sign(r) * sqrt(abs(q)) * math.sinh(t) - a / 3
            x_1 = complex(sign(r) * sqrt(abs(q)) * math.sinh(t) - a / 3, sqrt(3) * sqrt(abs(q)) * math.cosh(t))
            x_2 = complex(sign(r) * sqrt(abs(q)) * math.sinh(t) - a / 3, -sqrt(3) * sqrt(abs(q)) * math.cosh(t))
            text = 'X1 = %s\n X2 = %s\n X3 = %s\n' % (x_0, x_1, x_2)
            return text
    else:
        x_0 = -2 * sign(r) * sqrt(q) - a / 3
        x_1 = sign(r) * sqrt(q) - a / 3
        text = 'X1 = %s\n X2 = %s\n' % (x_0, x_1)
        return text