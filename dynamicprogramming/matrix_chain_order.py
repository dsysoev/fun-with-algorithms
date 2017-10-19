

"""
Consider the matrix chain algorithm in the following example.
We have a example matrix chain: [10, 100, 5, 50]
which represents a multiplication of three matrix
first matrix A1 with shape [10 x 100], second A2 [100 x 5], third A3 [5 x 50]

For this example, we have only 2 possible combinations
for matrix multiplication,
first multiply (A1 x A2) and then (A1A2 x A3)
the second (A2 x A3) and then (A1 x A2A3)

The computational cost of these operations is:
- (A1 x A2) x A3 = (10 * 100 * 5) + (10 * 5 * 50) = 7500
- A1 x (A2 x A3) = (10 * 100 * 50) + (100 * 5 * 50) = 75000

The matrix chain algorithm select operation with lower computational cost.
"""

from __future__ import print_function

def matrix_chain_order(chain):
    """ return a tuple (costs, midpoint)

        costs: list of list with shape (NxN) N = len(p) - 1
               matrix with number of operations it would take
               to multiply the sequence of matrices
        chain: an array of numbers,
               where chain[i] represents a side length of a matrix
    """
    num = len(chain) - 1
    # create an empty NxN cost matrix
    costs = [[0] * num for _ in range(num)]
    # create an empty NxN midpoint matrix
    mid = [[None] * (num) for _ in range(num)]
    # chain length
    for length in range(2, num + 1):
        # the 0-index of the start matrix
        for start in range(num - length + 1):
            # the 0-index of the end matrix
            end = start + length - 1
            costs[start][end] = float('inf')
            for midpoint in range(start, end):
                # calculate cost of multiplication
                # total cost equal to cost of left matrix plus right matrix
                # plus cost of multiplication left to right
                cost = (costs[start][midpoint] + costs[midpoint + 1][end] +
                        chain[start] * chain[midpoint + 1] * chain[end + 1])
                # if current cost is lower than costs
                if cost < costs[start][end]:
                    costs[start][end] = cost
                    mid[start][end] = midpoint
    return (costs, mid,)

def min_matrix_ops(chain):
    """ return minimum number of operations for current matrix chain """
    costs, _ = matrix_chain_order(chain)
    return costs[0][len(chain) - 2]

def get_optimal_parens(chain, mid, i, j):
    """ recursive algorithm for string presentation
        of optimal multiplication chain
    """
    if i == j:
        return '[' + str(chain[j]) + ' ' + str(chain[j + 1]) + ']'
    else:
        return ('(' + get_optimal_parens(chain, mid, i, mid[i][j]) +
                ' x ' + get_optimal_parens(chain, mid, mid[i][j] + 1, j) + ')')

def get_optimal_chain(chain):
    """ return string representation of matrix multiplication chain """
    _, mid = matrix_chain_order(chain)
    return get_optimal_parens(chain, mid, 0, len(chain) - 2)

if __name__ in '__main__':
    MATRIX_CHAIN = [10, 100, 5, 50]
    print('given matrix chain         :', MATRIX_CHAIN)
    print('minimum number of operation:', min_matrix_ops(MATRIX_CHAIN))
    print('matrix multiplication chain:', get_optimal_chain(MATRIX_CHAIN))
