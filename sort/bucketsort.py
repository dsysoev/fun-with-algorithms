# coding: utf-8

import math
from insertion import insertionsort

def bucketsort(lst):
    """ Implementation of bucket sort algorithm """

    # size of list
    n = len(lst)

    # return if list empty
    if n == 0:
        return lst

    # determine minimum and maximum values
    vmin, vmax = min(lst), max(lst)

    # the size of bucket
    bucketsize = 5

    # set the number of buckets
    number = int((vmax - vmin) / bucketsize) + 1

    # initialize buckets
    buckets = [[] for _ in range(number)]

    # distribute input array values into buckets
    for val in lst:
        # determine the bucket for given value
        ibucket = int((val - vmin) / bucketsize)
        # put value for given bucket
        buckets[ibucket].append(val)

    lst = []
    for i in range(len(buckets)):
        # sort bucket use insertion sort algorithm
        # it fast for small list sizes
        buckets[i] = insertionsort(buckets[i])
        # put sorted bucket back to list
        lst.extend(buckets[i])

    return lst

if __name__ in "__main__":

    a = [1, 0, 2, 4, 5, 6, 2, 7, 9, 1, 3, 8, -1]

    print('list          :', a)
    print('bucket sort   :', bucketsort(a), bucketsort(a) == sorted(a))
