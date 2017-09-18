# coding: utf-8

import timeit

import os
import numpy as np
import matplotlib.pyplot as plt

import argparse
import tempfile

import pandas as pd

from sort import insertion_sort, merge_sort

def get_performance_data():

    data = {'numbers': []}
    for i in range(1, FLAGS.max_degree + 1):

        n = 10 ** i
        min_max_value = n * 2
        a = np.random.randint(-min_max_value, min_max_value, size=(n)).tolist()

        data['numbers'].append(n)
        for algorithm, desc in [
                        ('insertion_sort', 'insertion sort O(n2)'),
                        ('merge_sort', 'merge sort O(n ln(n))')
                        ]:
            duration = timeit.Timer(
                algorithm + '({})'.format(a),
                """from __main__ import {}""".format(algorithm)
                ).timeit(number=10)
            if desc not in data:
                data[desc] = []
            data[desc].append(duration)

    return data

def plot_chart():
    """ Read result file and plot chart """
    # check results file
    if not os.path.isfile(FLAGS.results_file):
        raise IOError("No such file '{}'".format(FLAGS.results_file))

    # read DataFrame from results file
    results = pd.read_csv(FLAGS.results_file, index_col='numbers')

    # plot chart
    fig, ax = plt.subplots(1)
    for name in results.columns:
        (results[name] / results.index).plot(ax=ax)

    ax.set_title('Сomparison of sorting algorithms')
    ax.set_ylabel('time duration / length of list')
    ax.set_xlabel('length of list')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend()

    plt.show()

def main():

    if FLAGS.force or not os.path.isfile(FLAGS.results_file):
        if not os.path.isdir(os.path.dirname(FLAGS.results_file)):
            os.makedirs(os.path.dirname(FLAGS.results_file))
        data = get_performance_data()
        dataframe = pd.DataFrame(data).set_index('numbers')
        dataframe.to_csv(FLAGS.results_file, header=True)

    plot_chart()

if __name__ in "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--max_degree', type=int, default=3)
    parser.add_argument(
        '--results_file',
        type=str,
        default=os.path.join(tempfile.gettempdir(),
                             'fun-with-algorithms',
                             'sort.csv'),
        help='File with results')

    FLAGS, unparsed = parser.parse_known_args()
    main()
