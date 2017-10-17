
"""
Implementation of Josephus problem
https://en.wikipedia.org/wiki/Josephus_problem
"""

from __future__ import print_function

def josephus(num, k):
    """ recursive implementation of Josephus problem
        num - the number of people standing in the circle
        k - the position of the person who is to be killed

	    return the safe position who will survive the execution
    """
    if num == 1:
        return 1
    return (josephus(num - 1, k) + k - 1) % num + 1

if __name__ in '__main__':
    print(josephus(40, 3))
