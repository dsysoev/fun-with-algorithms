# coding: utf-8

import timeit
from multiprocessing.pool import ThreadPool

import os
import numpy as np
import matplotlib.pyplot as plt

import argparse
import tempfile

import pandas as pd

def insertion_sort(a):
    """ Function to sort an array using insertion sort algorithm """
    # start from second element of list
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        # insertion a[j] into sorted list a
        while i > 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a

def merge_sort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x) / 2)
        a = merge_sort(x[:middle])
        b = merge_sort(x[middle:])
    return merge(a, b)

def merge(a, b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:

        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])

    if len(a) == 0:
        c += b
    else:
        c += a

    return c

def calc_duration(n, func, number=10):
    """ Estimates execution time for list with n elements """
    instance = timeit.Timer(
            func + '(a)',
                """
import random
from __main__ import {0:}
a = [random.randint(0, {1:}) for _ in range({1:})]""".format(func, n))
    return instance.timeit(number=number)

def calc_duration_list(n_list, func, number):
    """ Calculate execution time for list of numbers """
    return [calc_duration(n, func, number) for n in n_list]

def create_data():
    """ Function considers execution time and return pandas.DataFrame object """
    n_list = [10 ** i for i in range(1, FLAGS.max_degree + 1)]

    tasks_list = [('insertion_sort', 'n ** 2'),
                  ('merge_sort', 'n * lg(n)')]

    pool = ThreadPool(processes=len(tasks_list))

    results = []
    # run in async
    for (func, desc) in tasks_list:
        results.append(pool.apply_async(calc_duration_list, (n_list, func, 10)))

    data = {'len': n_list}
    for i, (func, desc) in enumerate(tasks_list):
        data[func] = results[i].get()

    return pd.DataFrame(data).set_index('len')

def plot_chart():
    """ Read result file and plot chart """
    # check results file
    if not os.path.isfile(FLAGS.results_file):
        raise IOError("No such file '{}'".format(FLAGS.results_file))

    # read DataFrame from results file
    results = pd.read_csv(FLAGS.results_file, index_col='len')

    # plot chart
    fig, ax = plt.subplots(1)
    for name in results.columns:
        (results[name] / results.index).plot(ax=ax)

    ax.set_title('Сomparison of sorting algorithms')
    ax.set_ylabel('time duration / length of array')
    ax.set_xlabel('length of array')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend()

    plt.show()

def main():

    if FLAGS.force or not os.path.isfile(FLAGS.results_file):
        if not os.path.isdir(os.path.dirname(FLAGS.results_file)):
            os.makedirs(os.path.dirname(FLAGS.results_file))
        data = create_data()
        data.to_csv(FLAGS.results_file, header=True)

    plot_chart()

if __name__ in "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--max_degree', type=int, default=5)
    parser.add_argument(
        '--results_file',
        type=str,
        default=os.path.join(tempfile.gettempdir(),
                             'algorithms-book',
                             'sort.csv'),
        help='File with results')

    FLAGS, unparsed = parser.parse_known_args()
    main()
