# coding: utf-8

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x) / 2)
        # split the list into 2 branches
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
    # merge 2 branches
    return merge(a, b)

def merge(a, b):
    """ Function to merge two arrays """

    c = []
    while len(a) != 0 and len(b) != 0:

        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])

    if len(a) == 0:
        c += b
    else:
        c += a

    return c

if __name__ in "__main__":

    a = [1, 0, 2, 4, 5, 6, 2, 7, 9, 1, 3, 8, -1]

    print('list      :', a)
    print('merge sort:', mergesort(a), mergesort(a) == sorted(a))
