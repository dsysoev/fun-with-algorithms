# coding: utf-8

"""
Matrix multiplication
https://en.wikipedia.org/wiki/Matrix_multiplication#Parallel_matrix_multiplication

                     Average
Naive       T =         O(n^3)
Parallel    Tinfinity = O(n)
"""

from __future__ import print_function

import gevent


def naive_square_matrix_product(A, B):
    """ Implementation of naive squre matrix multiplication algorithm """
    shape = len(A)
    # determine zero matrix
    C = [[0 for _ in range(shape)] for _ in range(shape)]
    for i in range(shape):
        for j in range(shape):
            for k in range(shape):
                C[i][j] += A[i][k] * B[k][j]
    return C

def parallel_square_matrix_product(A, B):
    """ Implementation of parallel version of
        naive squre matrix multiplication algorithm
    """
    def calc_ij(i, j, shape, A, B, C):
        """ evaluate C[i,j] element in the matrix """
        for k in range(shape):
            C[i][j] += A[i][k] * B[k][j]

    shape = len(A)
    # determine zero matrix
    C = [[0 for _ in range(shape)] for _ in range(shape)]
    # determine list of threads
    threads = []
    for i in range(shape):
        # parallel for i
        for j in range(shape):
            # parallel for j
            threads.append(gevent.spawn(calc_ij, i, j, shape, A, B, C))
    # join all threads
    gevent.joinall(threads)
    return C

def print_mx(matrix):
    """ pretty print of matrix """
    for line in matrix:
        print("\t".join(map(str, line)))

if __name__ in "__main__":
    MATRIX1 = [[1, 2, 7, 0], [2, 3, 4, 2], [4, 5, 1, 0], [2, 6, 3, 8]]
    MATRIX2 = [[4, 5, 6, 1], [7, 6, 8, 0], [1, 0, 3, 6], [7, 4, 7, 5]]
    print('MATRIX A:')
    print_mx(MATRIX1)
    print('MATRIX B:')
    print_mx(MATRIX2)
    NAIVE = naive_square_matrix_product(MATRIX1, MATRIX2)
    OUT = parallel_square_matrix_product(MATRIX1, MATRIX2)
    print('Result A * B:')
    print_mx(OUT)
    print('correct:', NAIVE == OUT)
