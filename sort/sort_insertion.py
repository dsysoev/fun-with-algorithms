# coding: utf-8

def insertion_sort(a):
    """ Function to sort an array using insertion sort algorithm """
    # start from second element of list
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        # insertion a[j] into sorted list a
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a

if __name__ in "__main__":

    a = [1, 0, 2, 4, 5, 6, 2, 7, 9, 1, 3, 8, -1]

    print('insertion_sort', insertion_sort(a))
