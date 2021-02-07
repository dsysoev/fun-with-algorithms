

def insertionsort(lst):
    """ Implementation of insertion sort algorithm """
    # start from second element of list
    for j in range(1, len(lst)):
        key = lst[j]
        i = j - 1
        # insertion j-th into sorted list
        while i >= 0 and lst[i] > key:
            lst[i + 1] = lst[i]
            # select the previous item
            i -= 1
        lst[i + 1] = key
    return lst


if __name__ in "__main__":
    a = [1, 0, 2, 4, 5, 6, 2, 7, 9, 1, 3, 8, -1]
    print('list          :', a)
    print('insertion sort:', insertionsort(a), insertionsort(a) == sorted(a))
