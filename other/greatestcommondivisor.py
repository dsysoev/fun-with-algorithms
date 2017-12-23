

"""
Greatest common divisor
https://en.wikipedia.org/wiki/Greatest_common_divisor
"""

from __future__ import print_function


def euclid(val0, val1):
    """ Compute greatest common divisor using Euclid algorithm """
    if val1 == 0:
        return val0
    return euclid(val1, val0 % val1)

if __name__ in '__main__':
    print(euclid(30, 21))
