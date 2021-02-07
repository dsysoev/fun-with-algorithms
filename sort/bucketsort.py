# coding: utf-8

from insertionsort import insertionsort


def bucketsort(lst):
    """ Implementation of bucket sort algorithm """
    if not lst:
        return lst
    # determine minimum and maximum values
    vmin, vmax = min(lst), max(lst)
    # the size of bucket
    bucketsize = 5
    # set the number of buckets
    number = ((vmax - vmin) // bucketsize) + 1
    # initialize buckets
    buckets = [[] for _ in range(number)]
    # distribute input array values into buckets
    for val in iter(lst):
        # determine the bucket for given value
        ibucket = (val - vmin) // bucketsize
        # put value for given bucket
        buckets[ibucket].append(val)

    nls = []
    for i in range(len(buckets)):
        # sort bucket use insertion sort algorithm
        # it fast for small list sizes
        buckets[i] = insertionsort(buckets[i])
        # put sorted bucket back to list
        nls.extend(buckets[i])

    return nls

if __name__ in "__main__":

    a = [1, 0, 2, 4, 5, 6, 2, 7, 9, 1, 3, 8, -1]

    print('list          :', a)
    print('bucket sort   :', bucketsort(a), bucketsort(a) == sorted(a))
