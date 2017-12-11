

"""
Max heap implementation
https://en.wikipedia.org/wiki/Min-max_heap

Algorithm 	Average
Build heap  O(n)
"""

from __future__ import print_function

from math import log, ceil


class MaxHeap(object):
    """ Binary Max heap implementation """

    def __init__(self):
        self.__data = []

    def max_heapify(self, start):
        """ function with which to save the properties of the heap """
        left = self.left_child(start)
        right = self.right_child(start)
        size = self.heap_size()
        if left < size and self.__data[left] > self.__data[start]:
            largest = left
        elif right < size:
            largest = right
        else:
            return
        if right < size and self.__data[right] > self.__data[largest]:
            largest = right
        if largest != start and self.__data[start] < self.__data[largest]:
            self.__data[start], self.__data[largest] = self.__data[largest], self.__data[start]
            self.max_heapify(largest)

    def add_list(self, lst):
        """ add list of elements into the heap """
        self.__data += lst
        for index in range(self.parent(self.heap_size() - 1), -1, -1):
            self.max_heapify(index)

    def add(self, value):
        """ add one element into the heap """
        self.add_list([value])

    def extract_max(self):
        """ return maximum element from the heap """
        value = self.__data[0]
        del self.__data[0]
        for position in range(self.parent(self.heap_size() - 1), -1, -1):
            self.max_heapify(position)
        return value

    def heap_size(self):
        """ return number of elements in the heap """
        return len(self.__data)

    def parent(self, index):
        """ return parent index """
        return (index + 1) // 2 - 1

    def left_child(self, index):
        """ return index of left child """
        return 2 * index + 1

    def right_child(self, index):
        """ return index of right child """
        return 2 * index + 2

    def __str__(self):
        # string lenght for center
        strlen = 2 * 2 ** ceil(log(self.heap_size(), 2))
        maxlevel = int(log(self.heap_size(), 2)) + 1
        # add root element to string
        string = str([self.__data[0]]).center(strlen) + '\n'
        for index in range(1, maxlevel):
            # get list of elements for current level
            lst = self.__data[2 ** index - 1:2 ** (index + 1) - 1]
            if index == maxlevel - 1:
                # without center for last line
                string += str(lst) + '\n'
            else:
                string += str(lst).center(strlen) + '\n'
        return string


if __name__ in "__main__":
    HEAP = MaxHeap()
    LIST = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("Build heap from list: {}".format(LIST))
    HEAP.add_list(LIST)
    print("Show heap:\n{}".format(HEAP))
    for VALUE in [100]:
        print("Add new element {}".format(VALUE))
        HEAP.add(VALUE)
        print("Show heap:\n{}".format(HEAP))
    for _ in range(2):
        MAX = HEAP.extract_max()
        print("Extract max element: {}".format(MAX))
        print("Show heap:\n{}".format(HEAP))
