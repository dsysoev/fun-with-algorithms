
"""
Activity selection problem
https://en.wikipedia.org/wiki/Activity_selection_problem
"""

from __future__ import print_function


def activity_selection(start, finish):
    """ implementation of activity selection algorithm """
    # assumes that the activities
    # are already sorted according to their finish time
    # first activity is always selected
    lst = [0]
    k = 0
    for pid in range(1, len(start)):
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if start[pid] >= finish[k]:
            lst.append(pid)
            k = pid
    return lst

if __name__ in '__main__':
    # process id       0  1  2  3  4  5  6  7  8  9  10
    START_TIME_LIST = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    # assumes that the activities
    # are already sorted according to their finish time
    FINISH_TIME_LIST = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    PROCESS_ACTIVITY_LIST = activity_selection(START_TIME_LIST, FINISH_TIME_LIST)
    print('activity process id list: {}'.format(PROCESS_ACTIVITY_LIST))
    print('execution process:')
    for PROC in PROCESS_ACTIVITY_LIST:
        print('run process id {:2d} (start {:2d} -> {:2d} end time)'.format(
            PROC, START_TIME_LIST[PROC], FINISH_TIME_LIST[PROC]))
