# coding: utf-8

def naive_square_matrix_product(A, B):
    """ Implementation of naive squre matrix multiplication algorithm """
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def print_mx(matrix):
    """ pretty print of matrix """
    for line in matrix:
        print("\t".join(map(str, line)))


if __name__ in "__main__":

    a = [[1, 2, 7, 0], [2, 3, 4, 2], [4, 5, 1, 0], [2, 6, 3, 8]]
    b = [[4, 5, 6, 1], [7, 6, 8, 0], [1, 0, 3, 6], [7, 4, 7, 5]]

    naive = naive_square_matrix_product(a, b)
    print('naive algorithm')
    print_mx(naive)
