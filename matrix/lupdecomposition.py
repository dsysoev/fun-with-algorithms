
"""
LU decomposition implemented in python
https://en.wikipedia.org/wiki/LU_decomposition
"""

from __future__ import print_function


def print_mx(matrix):
    """ pretty print of matrix """
    for line in matrix:
        print("\t".join(map(str, line)))

def naive_matrix_product(A, B):
    """ Naive square matrix multiplication """
    msize = len(A)
    nsize = len(B[0])
    # determine zero matrix
    C = [[0 for _ in range(nsize)] for _ in range(msize)]
    for i in range(msize):
        for j in range(nsize):
            for k in range(msize):
                C[i][j] += A[i][k] * B[k][j]
    return C

def pivotize(matrix):
    """ Creates the pivoting matrix """
    size = len(matrix)
    # determine identity matrix P (n x n)
    P = [[float(i == j) for i in range(size)] for j in range(size)]
    r = 0
    for j in range(size):
        # find row with max element
        row = max(range(j, size), key=lambda i: abs(matrix[i][j]))
        if j != row:
            # swap current and max rows
            P[j], P[row] = P[row], P[j]
            r += 1
    return P, r

def lup_decomposition(A):
    """Decomposes a nxn matrix A by PA=LU and returns L, U and P."""
    n = len(A)
    # determine identity matrix (n x n)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1.
    # determine zero matrix (n x n)
    U = [[0.0] * n for _ in range(n)]
    # create pivoting matrix
    # for greater computational stability
    P, _ = pivotize(A)
    # calculate b = PA
    PA = naive_matrix_product(P, A)
    for j in range(n):
        # diagonal elements are equal
        U[j][j] = A[j][j]
        # calculate U (upper) triangle matrix
        for i in range(j + 1):
            summ = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - summ
        # calculate L (lower) triangle matrix
        for i in range(j, n):
            summ = sum(U[k][j] * L[i][k] for k in range(i))
            L[i][j] = (PA[i][j] - summ) / U[j][j]
    return L, U, P

def lup_solve(L, U, P, B):
    """ solve system of linear equations using LU-decomposiotion
        Ly = Pb
        Ux = y
    """
    num = len(L)
    # determine x, y
    x, y = [0.] * num, [0.] * num
    # multiply P*B for greater computational stability
    Pb = naive_matrix_product(P, B)
    for i in range(num):
        # calculate sum of multiplication lower (L) triangle matrix
        # and vector y
        summ = sum(L[i][j] * y[j] for j in range(num - 1))
        # current y[i] equal to Pb[i] - sum
        y[i] = Pb[i][0] - summ
    for i in reversed(range(num)):
        # go from the end to the beginning
        # calculate sum of multiplication upper (U) triangle matrix
        # and vertor x
        summ = sum(U[i][j] * x[j] for j in range(num))
        # current x[i] equal to y[i] - sum divided to U[i][i]
        x[i] = (y[i] - summ) / U[i][i]
    # convert list to matrix
    X = [[xi] for xi in x]
    return X

if __name__ in '__main__':
    # Ax = B
    # found x
    A = [[1, 2, 0], [3, 4, 4], [5, 6, 3]]
    B = [[3], [7], [8]]
    L, U, P = lup_decomposition(A)
    X = lup_solve(L, U, P, B)
    print('we have equation Ax = b')
    print('matrix A:')
    print_mx(A)
    print('matrix b:')
    print_mx(B)
    print('')
    print('perform LUP decomposition')
    print('matrix L:')
    print_mx(L)
    print('matrix U:')
    print_mx(U)
    print('matrix P:')
    print_mx(P)
    print('')
    print('solution of the linear equations:')
    print_mx(X)
