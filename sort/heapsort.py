# coding: utf-8

"""
Heapsort implementation
https://en.wikipedia.org/wiki/Heapsort

Worst-case performance 	O(n * log(n))
Best-case performance 	O(n)
Average performance 	O(n * log(n))
"""


def heapsort(lst):
    """ Implementation of heap sort algorithm """
    lenght = len(lst)
    heapstart = int(lenght / 2) - 1
    # build max heap part
    for start in range(heapstart, -1, -1):
        # build max heap
        max_heapify(lst, start, lenght - 1)
    # sorting part
    for end in range(lenght - 1, 0, -1):
        # zero element in heap has max value
        # we get zero element from the heap
        # and swap it with the end element in list
        lst[end], lst[0] = lst[0], lst[end]
        # restores heap properties
        # with list from zero to end - 1
        # storing sorted list after end - 1 element
        max_heapify(lst, 0, end - 1)
    return lst

def max_heapify(lst, start, end):
    """ performs permutation in a binary tree """

    root = start
    while True:
        # set child position from left branch
        child = root * 2 + 1
        # exit if child position outside the list
        if child > end:
            break
        # if right value bigger than left
        # change child position to right branch
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        # if root value lower than child
        if lst[root] < lst[child]:
            # swap root and child elements in list
            lst[root], lst[child] = lst[child], lst[root]
            # set new root
            root = child
        else:
            # otherwise exit
            break


if __name__ in "__main__":
    LIST = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print('list    :', LIST)
    print('heapsort:', heapsort(LIST))
