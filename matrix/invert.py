
def print_mx(matrix):
    """ pretty print of matrix """
    for line in matrix:
        print("\t".join(map(str, line)))

def invert(A):
    """ invert a square matrix A according to gauss-jordan elimination"""
    # get dimensions of A
    rows, cols = len(A), len(A[0])
    # set identity matrix
    identity = [[float(i == j) for i in range(cols)] for j in range(rows)]
    # append it to the right of A
    X = [A[i] + identity[i] for i in range(rows)]
    for n in range(cols):
        # check to see if there are any nonzero values
        # below the current row in the current column
        is_zeros, first_non_zero = check_for_all_zeros(X, n)
        if is_zeros:
            if n == cols:
                return A
            raise Exception("Matrix is singular")
        # if X[i][j] is 0, and there is a nonzero value below it,
        # swap the two rows
        if first_non_zero != n:
            X[first_non_zero], X[n] = X[n], X[first_non_zero]
        # divide X[i] by X[i][j] to make X[i][j] equal 1
        X[n] = [m / X[n][n] for m in X[n]]
        # rescale all other rows to make their values 0 below X[i][j]
        for q in range(rows):
            if q == n:
                continue
            scaled_row = [X[q][n] * m for m in X[n]]
            X[q] = [X[q][m] - scaled_row[m] for m in range(len(scaled_row))]
    # the right hand matrix is now our inverse
    return list(map(lambda x: x[cols:], X))

def check_for_all_zeros(X, n):
    is_zero_sum = True
    first_non_zero = -1
    for m in range(n, len(X)):
        if X[m][n] != 0:
            is_zero_sum = False
            if first_non_zero == -1:
                first_non_zero = m
                break
    return is_zero_sum, first_non_zero

if __name__ in "__main__":

    from multiplication import naive_square_matrix_product

    a = [[1, 5, 3, 2], [1, 4, 3, 4], [1, 3, 4, 10], [2, 5, 3, 8]]
    inv = invert(a)
    a_ = naive_square_matrix_product(a, inv)

    print('A:')
    print_mx(a)
    print("A':")
    print_mx(inv)
    print("A*A':")
    print_mx(a_)
