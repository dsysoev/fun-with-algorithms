
"""
Naive string matcher implementation
"""

from __future__ import print_function


def naive_string_matcher(string, target):
    """ returns all indices where substring target occurs in string """
    snum = len(string)
    tnum = len(target)
    matchlist = []
    for index in range(snum - tnum + 1):
        if string[index:index + tnum] == target:
            matchlist.append(index)
    return matchlist

if __name__ in '__main__':
    for STR, TARGET in [
            ('abcdefabcdeab', 'ab'),
            ('abababcdefabcdeab', 'abab'),
            ('ababcdefabcdeab', 'abc'),
            ('abcdefabcdeab', 'c'),
            ('abcdefabcdeab', 'abcde'),
            ]:
        POS = naive_string_matcher(STR, TARGET)
        print('string: {:20s} target: {:5s} positions: {}'.format(STR, TARGET, POS))
