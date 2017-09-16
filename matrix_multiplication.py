# coding: utf-8

def naive_square_matrix_product(A, B):
    """ Implementation of naive squre matrix multiplication algorithm """
    n = len(A)
    C = zeros_matrix((n, n))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def print_mx(matrix):
    """ pretty print of matrix """
    for line in matrix:
        print("\t".join(map(str, line)))

def shape_mx(A):
    """ shape of matrix """
    return (len(A), len(A[0]))

def add(A, B):
    """ Implementation of summation of two matrix """
    n = len(A)
    C = zeros_matrix((n, n))
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtract(A, B):
    """ Implementation of subtraction of two matrix """
    n = len(A)
    C = zeros_matrix((n, n))
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def zeros_matrix(shape):
    """ create zero matrix with define shape """
    return [[0 for j in range(0, shape[1])] for i in range(0, shape[0])]

def strassen_square_matrix_product(A, B):
    """ Implementation of the strassen algorithm for square matrixes"""
    n = len(A)

    # the size of matrix when we start using naive square maxtrix product
    LEAF_SIZE = 2

    if n <= LEAF_SIZE:
        return naive_square_matrix_product(A, B)

    # initializing the new sub-matrices
    new_size = n // 2

    a11 = zeros_matrix((new_size, new_size))
    a12 = zeros_matrix((new_size, new_size))
    a21 = zeros_matrix((new_size, new_size))
    a22 = zeros_matrix((new_size, new_size))

    b11 = zeros_matrix((new_size, new_size))
    b12 = zeros_matrix((new_size, new_size))
    b21 = zeros_matrix((new_size, new_size))
    b22 = zeros_matrix((new_size, new_size))

    # dividing the matrices in 4 sub-matrices:
    for i in range(0, new_size):
        for j in range(0, new_size):
            a11[i][j] = A[i][j]                         # top left
            a12[i][j] = A[i][j + new_size]              # top right
            a21[i][j] = A[i + new_size][j]              # bottom left
            a22[i][j] = A[i + new_size][j + new_size]   # bottom right
            b11[i][j] = B[i][j]                         # top left
            b12[i][j] = B[i][j + new_size]              # top right
            b21[i][j] = B[i + new_size][j]              # bottom left
            b22[i][j] = B[i + new_size][j + new_size]   # bottom right

    # Calculating p1 to p7:
    # p1 = (a11) * (b12 - b22)
    p1 = strassen_square_matrix_product(a11, subtract(b12, b22))
    # p2 = (a11 + a12) * (b22)
    p2 = strassen_square_matrix_product(add(a11, a12), b22)
    # p3 = (a21 + a22) * (b11)
    p3 = strassen_square_matrix_product(add(a21, a22), b11)
    # p4 = (a22) * (b21 - b11)
    p4 = strassen_square_matrix_product(a22, subtract(b21, b11))
    # p5 = (a11 + a22) * (b11 + b22)
    p5 = strassen_square_matrix_product(add(a11, a22), add(b11, b22))
    # p6 = (a12 - a22) * (b21 + b22)
    p6 = strassen_square_matrix_product(subtract(a12, a22), add(b21, b22))
    # p7 = (a11 - a21) * (b11 + b12)
    p7 = strassen_square_matrix_product(subtract(a11, a21), add(b11, b12))

    # calculating c11 to c22:
    # c11 = p5 + p4 - p2 + p6
    c11 = add(subtract(add(p5, p4), p2), p6)
    # c12 = p1 + p2
    c12 = add(p1, p2)
    # c21 = p3 + p4
    c21 = add(p3, p4)
    # c22 = p5 + p1 - p3 - p7
    c22 = subtract(subtract(add(p5, p1), p3), p7)

    # grouping the results obtained to single matrix
    C = zeros_matrix((n, n))
    for i in range(0, new_size):
        for j in range(0, new_size):
            C[i][j] = c11[i][j]
            C[i][j + new_size] = c12[i][j]
            C[i + new_size][j] = c21[i][j]
            C[i + new_size][j + new_size] = c22[i][j]

    return C

a = [[1, 2, 7, 0], [2, 3, 4, 2], [4, 5, 1, 0], [2, 6, 3, 8]]
b = [[4, 5, 6, 1], [7, 6, 8, 0], [1, 0, 3, 6], [7, 4, 7, 5]]

naive = naive_square_matrix_product(a, b)
print('naive algorithm')
print_mx(naive)
print('Strassen algorithm')
strassen = strassen_square_matrix_product(a, b)
print_mx(strassen)
