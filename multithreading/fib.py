
"""
The worst way to calculate Fibonacci numbers
to demonstrate the concept of a multithreaded algorithm
https://en.wikipedia.org/wiki/Fibonacci_number
"""

from __future__ import print_function

import gevent


def fib(num):
    """ the worst implementation of Fibonacci numbers calculation
        complexity: T(N) = O(a ^ N), a - constant

    Parameters
    ----------
    num : int
          requested Fibonacci number

    Returns
    -------
    out : int
          Fibonacci number

    """
    if num < 2:
        return num
    val1 = fib(num - 1)
    val2 = fib(num - 2)
    return val1 + val2

def fib_parallel(num):
    """ the worst implementation of Fibonacci numbers calculation
        using multithreading
        complexity: Tinfinity(N) = O(N)

    Parameters
    ----------
    num : int
          requested Fibonacci number

    Returns
    -------
    out : int
          Fibonacci number

    """
    if num < 2:
        return num
    # set new thread
    thread = gevent.spawn(fib_parallel, num - 1)
    # evaluate val2 in current thread
    val2 = fib_parallel(num - 2)
    # get result from thread
    val1 = thread.get()
    # all threads are synchronized
    return val1 + val2

if __name__ == '__main__':
    for N in range(11):
        print('Fib number: {} value: {}'.format(N, fib_parallel(N)))
