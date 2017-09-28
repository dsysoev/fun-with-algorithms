# coding: utf-8

def heapsort(ls):
    """ Implementation of heap sort algorithm """

    l = len(ls)
    heap_start = int(l / 2) - 1
    for start in range(heap_start, -1, -1):
        max_heapify(ls, start, l - 1)

    for end in range(l - 1, 0, -1):
        ls[end], ls[0] = ls[0], ls[end]
        max_heapify(ls, 0, end - 1)

    return ls

def max_heapify(ls, start, end):
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
        if child + 1 <= end and ls[child] < ls[child + 1]:
            child += 1
        # if root value lower than child
        if ls[root] < ls[child]:
            # swap root and child elements in list
            ls[root], ls[child] = ls[child], ls[root]
            # set new root
            root = child
        else:
            # otherwise exit
            break

if __name__ in "__main__":

    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

    print('list    :', a)
    print('heapsort:', heapsort(a), heapsort(a) == sorted(a))
