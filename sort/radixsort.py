# coding: utf-8


def radixsort(lst):
    """ Implementation of radix sort algorithm """

    # number system
    r = 10
    maxLen = 11
    for x in range(maxLen):
        # initialize bins
        bins = [[] for i in range(r + 9)]

        for y in lst:
            # more or equal zero
            if y >= 0:
                bins[int(y / 10 ** x) % r + 9].append(y)
            else:
                # otherwise
                bins[int(y / 10 ** x) % r].append(y)

        lst = []
        # apply bins to list
        for section in bins:
            lst.extend(section)
            
    return lst


if __name__ in "__main__":
    a = [1, 0, 2, 4, 5, 6, 2, 7, 9, 1, 3, 8, -1]
    print('list            :', a)
    print('radixsort       :', radixsort(a), radixsort(a) == sorted(a))
