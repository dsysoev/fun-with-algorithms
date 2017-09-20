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

def shape_mx(A):
    """ shape of matrix """
    return (len(A), len(A[0]))

def subtract(A, B):
    num = len(A[0])
    a_ = [val for sub in A for val in sub]
    b_ = [val for sub in B for val in sub]
    ab_ = [x - y for x, y in zip(a_, b_)]
    return [ab_[i * num:num + i * num] for i in range(num)]

def add(A, B):
    num = len(A[0])
    a_ = [val for sub in A for val in sub]
    b_ = [val for sub in B for val in sub]
    ab_ = [x + y for x, y in zip(a_, b_)]
    return [ab_[i * num:num + i * num] for i in range(num)]

def strassen_square_matrix_product(A, B, leaf_size=64):
    """ Implementation of the strassen algorithm for square matrixes"""

    n = len(A)
    # the size of matrix when we start using naive square maxtrix product
    if n <= leaf_size:
        return naive_square_matrix_product(A, B)

    # initializing the new sub-matrices
    new_size = n // 2

    a11 = list(map(lambda x: x[:new_size], A[:new_size]))      # top left
    a12 = list(map(lambda x: x[new_size:], A[:new_size]))      # top right
    a21 = list(map(lambda x: x[:new_size], A[new_size:]))      # bottom left
    a22 = list(map(lambda x: x[new_size:], A[new_size:]))      # bottom right

    b11 = list(map(lambda x: x[:new_size], B[:new_size]))      # top left
    b12 = list(map(lambda x: x[new_size:], B[:new_size]))      # top right
    b21 = list(map(lambda x: x[:new_size], B[new_size:]))      # bottom left
    b22 = list(map(lambda x: x[new_size:], B[new_size:]))      # bottom right

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

    cl = c11 + c21
    cr = c12 + c22
    return [cl[i] + cr[i] for i in range(len(cl))]

if __name__ in "__main__":

    a = [[1, 2, 7, 0], [2, 3, 4, 2], [4, 5, 1, 0], [2, 6, 3, 8]]
    b = [[4, 5, 6, 1], [7, 6, 8, 0], [1, 0, 3, 6], [7, 4, 7, 5]]

    print('Strassen algorithm')
    strassen = strassen_square_matrix_product(a, b)
    print_mx(strassen)
