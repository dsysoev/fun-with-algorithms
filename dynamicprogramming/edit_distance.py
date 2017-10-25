

"""
simple implementation of Levenshtein distance algorithm
https://en.wikipedia.org/wiki/Levenshtein_distance

example:
ABC, ABF = 1
ABC, CBA = 2
"""

from __future__ import print_function

def levenshtein_matrix(str1, str2):
    """ return levenshtein distance matrix (len(str1) x len(str2)) """
    if len(str2) == 0:
        return len(str1)
    elif len(str1) == 0:
        return len(str2)
    # set matrix with single row
    matrix = [list(range(len(str2) + 1))]
    for i, char1 in enumerate(str1):
        # set current row
        current = [i + 1]
        # get previous row
        previous = matrix[i]
        for j, char2 in enumerate(str2):
            # calculate costs
            insertions = previous[j + 1] + 1
            deletions = current[j] + 1
            substitutions = previous[j] + (char1 != char2)
            # add operation with lowest cost
            current.append(min(insertions, deletions, substitutions))
        # add current row
        matrix.append(current)
    return matrix

def edit_distance(str1, str2):
    """ return number of Levenshtein distance between two words """
    return levenshtein_matrix(str1, str2)[-1][-1]

def print_prescription(str1, str2):
    """ return string prescription between two words """
    matrix = levenshtein_matrix(str1, str2)

    prescription = []
    prescription1 = []
    prescription2 = []
    i, j = len(str1), len(str2)

    while i and j:
        insert = matrix[i][j - 1]
        delete = matrix[i - 1][j]
        match_or_replace = matrix[i - 1][j - 1]
        best_choice = min(insert, delete, match_or_replace)
        if best_choice == match_or_replace:
            if str1[i - 1] == str2[j - 1]:
                # match
                prescription.append('+')
            else:
                # replace
                prescription.append('-')
            prescription1.append(str1[i - 1])
            prescription2.append(str2[j - 1])
            i -= 1
            j -= 1
        elif best_choice == insert:
            prescription.append('*')
            prescription1.append(' ')
            prescription2.append(str2[j - 1])
            j -= 1
        elif best_choice == delete:
            prescription.append('-')
            prescription1.append(str1[i - 1])
            prescription2.append(' ')
            i -= 1
    # change the reverse order to the direct
    prescription.reverse()
    prescription1.reverse()
    prescription2.reverse()

    return (''.join(prescription1) + '\n' +
            ''.join(prescription2) + '\n' + ''.join(prescription))


if __name__ in '__main__':
    WORD1, WORD2 = 'GATCGGCAT', 'CAATGTGAATC'
    DISTANCE = edit_distance(WORD1, WORD2)
    print("edit distance \'{}\' \'{}\':".format(WORD1, WORD2), DISTANCE, '\n')
    print('prescription:')
    print(print_prescription(WORD1, WORD2))
