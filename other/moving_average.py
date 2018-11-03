
"""
Simple moving average (SMA) implementation
https://en.wikipedia.org/wiki/Moving_average
"""

from __future__ import print_function


def moving_average(lst, size):
    """ calculate simple moving average values """
    if not isinstance(size, int):
        raise TypeError('size must be integer. {} given'.format(size))
    if not size > 0:
        raise ValueError('size must be greater than zero. {} given'.format(size))
    if len(lst) < size:
        raise ValueError(('length of list must be greater than size.'
                          ' list: {} size: {}'.format(lst, size)))
    summ = sum(lst[:size])
    nlst = [summ / size]
    for end in range(size, len(lst)):
        summ += lst[end] - lst[end - size]
        nlst.append(summ / size)
    return nlst

if __name__ in '__main__':
    LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('{:36s}: {}'.format('list', LIST))
    for SIZE in [2, 3]:
        MOVAVG = moving_average(LIST, SIZE)
        string = 'moving average (window size = {})'.format(SIZE)
        print('{:36s}: {}'.format(string, MOVAVG))
