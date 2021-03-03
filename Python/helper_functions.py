import numpy as np

def norm_1(U, h):
    sum = 0
    for i in range(len(U)):
        sum += U[i]
    return sum * h


def norm_1_two(U1, U2, h):
    sum = 0
    for i in range(len(U1)):
        sum += np.abs(U1[i] - U2[i])
    return sum * h