# coding: utf-8

"""
simple implementation of Longest common subsequence algorithm
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
"""

from __future__ import print_function

def lcs_length(str1, str2):
    """ get longest common subsequence length
        str1, str2 - strings

        return C, B - matrix (M+1xN+1)
    """
    len1 = len(str1)
    len2 = len(str2)
    # determine zero matrix
    C = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    B = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i, char1 in enumerate(str1):
        for j, char2 in enumerate(str2):
            if char1 == char2:
                # increase next item
                C[i + 1][j + 1] = C[i][j] + 1
                B[i + 1][j + 1] = '↖'
            elif C[i][j + 1] >= C[i + 1][j]:
                C[i + 1][j + 1] = C[i][j + 1]
                B[i + 1][j + 1] = '↑'
            else:
                C[i + 1][j + 1] = C[i + 1][j]
                B[i + 1][j + 1] = '←'
    return C, B

def print_lcs(B, str1, i, j):
    """ recursive print lcs funtion """
    if i == 0 or j == 0:
        return ''
    if B[i][j] == '↖':
        return str(print_lcs(B, str1, i - 1, j - 1)) + str(str1[i - 1])
    elif B[i][j] == '↑':
        return str(print_lcs(B, str1, i - 1, j))
    else:
        return str(print_lcs(B, str1, i, j - 1))

def lcs(str1, str2):
    """ longest common subsequence algorithm implementation """
    _, B = lcs_length(str1, str2)
    return print_lcs(B, str1, len(str1), len(str2))

if __name__ in '__main__':
    for WORD1, WORD2 in [('thisisatest', 'testing123testing'),
                         ('ABCBDAB', 'BDCABA')]:
        SUB = lcs(WORD1, WORD2)
        print('LCS between words \'{}\' \'{}\':'.format(WORD1, WORD2), SUB)
