"""
Implementation of comb sort algorithm
https://en.wikipedia.org/wiki/Comb_sort
"""


def combsort(lst):
    size = len(lst)
    # set initial gap
    gap = size
    swaps = True

    while gap > 1 or swaps:
        # Minimun gap is 1
        gap = max(1, int(gap / 1.25))
        swaps = False

        for i in range(size - gap):
            j = i + gap

            if lst[i] > lst[j]:
                # swap elements
                lst[i], lst[j] = lst[j], lst[i]
                swaps = True
    return lst


if __name__ in "__main__":
    LIST = [1, 0, 2, 4, 5, 6, 2, 7, 9, 1, 3, 8, -1]
    print('list        :', LIST)
    print('comb sort   :', combsort(LIST), combsort(LIST) == sorted(LIST))
