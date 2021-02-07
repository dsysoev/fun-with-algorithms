import random
from quicksort import partition


def select_statistic_random(lst, start, end, i):
    """ select i-statistic algorithm use random element everytime """
    if start >= end:
        return lst[start]
    # select random pivot element
    pivot = random.randint(start, end)
    # swap pivot and last element into list
    lst[-1], lst[pivot] = lst[-1], lst[pivot]
    # regrouping the list
    new_pivot = partition(lst, start, end)
    k = new_pivot - start + 1
    if i == k:
        return lst[new_pivot]
    elif i < k:
        # run recursive quick sort for left half
        return select_statistic_random(lst, start, new_pivot - 1, i)
    else:
        # run for right half
        return select_statistic_random(lst, new_pivot + 1, end, i - k)


def select_statistic(lst, i):
    """ Implementation of select i-statistic algorithm with random pivot """
    if i > len(lst):
        raise Exception('i-statistic should be from 0 to {} ({} given)'.format(len(lst) - 1, i))

    return select_statistic_random(lst, 0, len(lst) - 1, i + 1)


if __name__ in "__main__":

    a = [2, 8, 7, 1, 3, 5, 6, 4]
    i = 7

    print('list            :', a)
    print('statistic number:', i)
    print('statistic value :', select_statistic(a, i), select_statistic(a, i) == sorted(a)[i])
