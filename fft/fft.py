
"""
Fast Fourier transform
https://en.wikipedia.org/wiki/Fast_Fourier_transform
"""

from __future__ import print_function

from cmath import exp, pi


def fft(x):
    """Compute the discrete Fourier Transform"""
    num = len(x)
    if num <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    y = [0.] * num
    for k in range(num // 2):
        t = exp(-2j * pi * k / num) * odd[k]
        y[k] = even[k] + t
        y[k + num // 2] = even[k] - t
    return y

if __name__ in '__main__':
    LIST = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    print(' '.join("{}".format(f) for f in fft(LIST)))
