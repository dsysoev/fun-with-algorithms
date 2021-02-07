# coding: utf-8

"""
Merge sort implementation
https://en.wikipedia.org/wiki/Merge_sort
"""

from __future__ import print_function


def mergesort(lst):
    """ Function to sort an array using merge sort algorithm

    Parameters
    ----------
    lst : list
          sorting list

    Returns
    -------
    out : list
          sorted list

    """
    if len(lst) < 2:
        return lst
    # determine middle element in the list
    middle = len(lst) // 2
    # split the list into 2 list
    # and sort it
    lst1 = mergesort(lst[:middle])
    lst2 = mergesort(lst[middle:])
    # merge 2 lists
    return merge(lst1, lst2)

def merge(lst1, lst2):
    """ Function to merge two sorted lists into list """
    lst = []
    while len(lst1) != 0 and len(lst2) != 0:
        # loop until lists are not empty
        if lst1[0] < lst2[0]:
            # append lower element to list
            lst.append(lst1[0])
            # remove it
            lst1.remove(lst1[0])
        else:
            # append element and remove it
            lst.append(lst2[0])
            lst2.remove(lst2[0])
    # adds the rest of the list
    if len(lst1) == 0:
        lst += lst2
    else:
        lst += lst1
    return lst


if __name__ in "__main__":
    LIST = [1, 0, 2, 4, 5, 6, 2, 7, 9, 1, 3, 8, -1]
    print('list      :', LIST)
    print('merge sort:', mergesort(LIST))
