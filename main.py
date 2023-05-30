from math import sqrt

def quadcc(a ,b, c):
    if (a == 0) and (b == 0):
        return None, None
    if (a == 0) and (b != 0):
        return -c / b, None
    d = ((b * b) - (4 * a * c))
    if d < 0:
        return None, None
    x1 = (b*(-1) + sqrt(d)) / (2 * a)
    x2 = (b*(-1) - sqrt(d)) / (2 * a)
    if d == 0:
        x2 = None
    return x1, x2