

""" Implementation of knapsack 0/1 problem
    https://en.wikipedia.org/wiki/Knapsack_problem
"""

from __future__ import print_function

def knapsack_matrix(items, limit):
    """ value matrix for knapsack problem

        items - list(name, weight, value)
        limit - maximum weight of knapsack

        return matrix NxM (N - len(item) + 1, M - limit + 1 )
    """
    # set zero matrix
    # rows equal limit weight, columns - items
    matrix = [[0] * (limit + 1) for _ in range(len(items) + 1)]
    # start from second row
    for i in range(1, len(items) + 1):
        # get name, weight and value for current item
        _, weight, value = items[i - 1]
        # start from second column
        for w in range(1, limit + 1):
            if weight > w:
                # copy value from previous item for current weight
                matrix[i][w] = matrix[i - 1][w]
            else:
                # choose the most valuable set
                # option 1: use value from previous item for current weight
                # option 2: from the previous item for the remaining weight
                #           plus current value
                matrix[i][w] = max(matrix[i - 1][w],
                                   matrix[i - 1][w - weight] + value)

    return matrix

def knapsack_items(items, limit):
    """ return list with items name for current knapsack """
    matrix = knapsack_matrix(items, limit)
    result = []
    w = limit
    for j in range(len(items), 0, -1):
        # determine whether j was added
        was_added = matrix[j][w] != matrix[j - 1][w]
        if was_added:
            name, weight, _ = items[j - 1]
            # add name to result
            result.append(name)
            w -= weight

    return result

def knapsack_value(items, limit):
    """ return value of current knapsack """
    matrix = knapsack_matrix(items, limit)
    return matrix[len(items)][limit]

def knapsack_weight(items, limit):
    """ return weight for current knapsack """
    matrix = knapsack_matrix(items, limit)
    w = limit
    for j in range(len(items), 0, -1):
        # determine whether j was added
        was_added = matrix[j][w] != matrix[j - 1][w]
        if was_added:
            _, weight, _ = items[j - 1]
            w -= weight
    return limit - w

if __name__ in '__main__':
    # items (name, weight, value)
    ITEMS = [('apple', 10, 100), ('watch', 3, 400), ('phone', 5, 500),
             ('milk', 20, 300)]
    MAX_WEIGHT = 10
    print('knapsack items :', knapsack_items(ITEMS, MAX_WEIGHT))
    print('knapsack value :', knapsack_value(ITEMS, MAX_WEIGHT))
    print('knapsack weight:', knapsack_weight(ITEMS, MAX_WEIGHT))
