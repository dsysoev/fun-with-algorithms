# coding: utf-8

"""
Performance comparison of different method to finding Fibonacci numbers
https://en.wikipedia.org/wiki/Fibonacci_number
"""

import sys
from time import time
from functools import lru_cache
from functools import wraps

import numpy as np


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        value = func(*args, **kwargs)
        end_ = int(round(time() * 1000)) - start
        return value, end_

    return _time_it


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


@measure
def fib_dynamic(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


@measure
def fib_cache(n):
    return fib(n)


@measure
def fib_matrix(n):
    qmatrix = np.matrix([[1, 1], [1, 0]], dtype=object)
    return (qmatrix ** n)[0, 1]


@measure
def fib_golden_ratio(n):
    evals = [(1+np.sqrt(5))/2, (1-np.sqrt(5))/2]
    return int((evals[0]**n - evals[1]**n) / np.sqrt(5))


if __name__ in '__main__':
    sys.setrecursionlimit(40000)

    for func, fnum_list in [
        (fib_golden_ratio, [1e2, 1e3]),
        (fib_cache, [1e2, 1e3, 1e4]),
        (fib_dynamic, [1e2, 1e3, 1e4, 1e5, 1e6]),
        (fib_matrix, [1e2, 1e3, 1e4, 1e5, 1e6])
        ]:
        print('\nFunction {}'.format(func.__name__))
        for fnumber in fnum_list:
            value, evaltime = func(int(fnumber))
            print(('{:7d} fibonacci number: {} ms'
            .format(int(fnumber), evaltime)))
