

""" Implementation of fractional knapsack problem
    https://en.wikipedia.org/wiki/Continuous_knapsack_problem
"""

from __future__ import print_function

def knapsack(items, limit):
    """ implementation of fractional knapsack problem

        items - list(name, weight, value)
        limit - maximum weight of knapsack

        return list (name, weight)
    """
    # calculate relative value for each item
    relative = []
    for name, weight, value in items:
        relative.append((name, value / weight, weight))
    # start from most valuable item
    relative.sort(key=lambda x: x[1], reverse=True)

    result = []
    w = limit
    for name, _, weight in relative:
        if weight > w:
            # last item
            result.append((name, w))
            break
        else:
            # add item completely
            result.append((name, weight))
            # reduce the free weight in the knapsack
            w -= weight
    return result

if __name__ in '__main__':
    # items (name, weight, value)
    ITEMS = [('apple', 10, 100), ('watch', 3, 400), ('phone', 5, 500),
             ('milk', 20, 300)]
    MAX_WEIGHT = 10
    print('knapsack :', knapsack(ITEMS, MAX_WEIGHT))
