# coding: utf-8


def counting_sort(lst, vmin, vmax):
    """ Implementation of counting sort algorithm recursive function """

    # create additional frequencies list
    freq = [0] * (vmax - vmin + 1)
    for x in lst:
        # increase the counter for current value
        freq[x - vmin] += 1

    nls = []
    # going over frequencies
    for x, n in enumerate(freq):
        # add value (x + vmin) n times to new list
        nls.extend([x + vmin] * n)

    return nls


def countingsort(lst):
    """ Implementation of counting sort algorithm """
    if not lst:
        return lst
    return counting_sort(lst, min(lst), max(lst))


if __name__ in "__main__":
    a = [1, 0, 2, 4, 5, 6, 2, 7, 9, 1, 3, 8, -1]
    print('list            :', a)
    print('counting sort   :', countingsort(a), countingsort(a) == sorted(a))
