import numpy as np


def horner(n, tab):
    result = 0
    for i in tab:
        result = result * n + i
    return result

def function(x, flag):
    fx = 0.0
    if flag == '1':
        parameters = [2,3,4, -1]    # 2x^3+3x^2+4x-1
        fx = horner(x, parameters)
    if flag == '2':
        fx = 2 * np.cos(x) + np.sin(x)   # cos(x) + sin(x)
    if flag == '3':
        fx = 5 ** x - 4
    if flag == '4':
        parameters = [1, 0, 0, 0]
        fx = horner(x, parameters) + 2**x - np.cos(x)  # x^3 + 2^x - cos(x)
    return fx


