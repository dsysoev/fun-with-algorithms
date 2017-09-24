# coding: utf-8

def transpose(A):
    """ returns the transpose of matrix A. """
    return list(map(list, zip(*A)))

if __name__ in "__main__":
    a = [[1, 2], [3, 4], [5, 6]]
    print('A:')
    print(a)
    print('AT:')
    print(transpose(a))
