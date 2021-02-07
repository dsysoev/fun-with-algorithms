# coding: utf-8

import random


def partition(lst, start, end):
    """
    move elements below pivot value to left half of list and bigger to right half
    return the new position of the pivot element
    """
    # use pivot as the last element in list
    # get it value
    x = lst[end]
    # initial store_index
    store_index = start
    # loop up to pivot (last element)
    i = start
    for i in range(start, end):
        # if current value below pivot
        if lst[i] <= x:
            # swap index and store_index elements if are differ
            if i != store_index:
                lst[i], lst[store_index] = lst[store_index], lst[i]
            # update store_index
            store_index += 1
    # swap pivot element (last in list) and store_index
    lst[store_index], lst[i + 1] = lst[i + 1], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    """ quick sort algorithm always use last element as pivot """
    if start >= end:
        return lst
    # regrouping the list
    new_pivot = partition(lst, start, end)
    # run recursive quick sort for left half
    quick_sort(lst, start, new_pivot - 1)
    # run for right half
    quick_sort(lst, new_pivot + 1, end)


def quick_sort_median(lst, start, end):
    """ quick sort algorithm use meadian value element"""

    if start >= end:
        return lst

    # for list more than 30 elements
    # use median value
    elif end - start >= 30:
        # create dict for select pivot element
        # keys --> values of lst, values --> index in lst
        median_values = {}
        while len(median_values) < 3:
            # select random element
            rand = random.randint(start, end)
            median_values[lst[rand]] = rand
        # select median element
        pivot_value = list(median_values.keys())[1]
        # get pivot index
        pivot = median_values[pivot_value]

    else:
        pivot = random.randint(start, end)

    # swap pivot and last element into list
    lst[-1], lst[pivot] = lst[-1], lst[pivot]
    # regrouping the list
    new_pivot = partition(lst, start, end)
    # run recursive quick sort for left half
    quick_sort_median(lst, start, new_pivot - 1)
    # run for right half
    quick_sort_median(lst, new_pivot + 1, end)


def quick_sort_random(lst, start, end):
    """ random quick sort algorithm use random element everytime """
    if start >= end:
        return lst
    # select random pivot element
    pivot = random.randint(start, end)
    # swap pivot and last element into list
    lst[-1], lst[pivot] = lst[-1], lst[pivot]
    # regrouping the list
    new_pivot = partition(lst, start, end)
    # run recursive quick sort for left half
    quick_sort_random(lst, start, new_pivot - 1)
    # run for right half
    quick_sort_random(lst, new_pivot + 1, end)


def quicksort(lst):
    """ Implementation of quicksort algorithm with constant pivot """
    quick_sort(lst, 0, len(lst) - 1)
    return lst


def quicksort_random(lst):
    """ Implementation of quicksort algorithm with random pivot """
    quick_sort_random(lst, 0, len(lst) - 1)
    return lst


def quicksort_median(lst):
    """ Implementation of quicksort algorithm with random pivot """
    quick_sort_median(lst, 0, len(lst) - 1)
    return lst


if __name__ in "__main__":
    a = [2, 8, 7, 1, 3, 5, 6, 4]
    print('list            :', a)
    print('quicksort       :', quicksort(a), quicksort(a) == sorted(a))
    print('quicksort random:', quicksort_random(a), quicksort_random(a) == sorted(a))
    print('quicksort median:', quicksort_median(a), quicksort_median(a) == sorted(a))
