
"""
Simple moving average (SMA) implementation
https://en.wikipedia.org/wiki/Moving_average
"""

from __future__ import print_function


def moving_average(lst, num):
    """ calculate simple moving average values """
    if len(lst) < num or num < 1:
        return []
    summ = sum(lst[:num])
    nlst = [summ / num]
    for end in range(num, len(lst)):
        summ += lst[end] - lst[end - num]
        nlst.append(summ / num)
    return nlst

if __name__ in '__main__':
    NUM = 2
    LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    MOVAVG = moving_average(LIST, NUM)
    print('list: {}'.format(LIST))
    print('moving average number={} : {}'.format(NUM, MOVAVG))
