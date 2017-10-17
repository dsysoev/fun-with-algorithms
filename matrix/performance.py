# coding: utf-8

import os
import timeit
import tempfile
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib

matplotlib.style.use('seaborn')

from multiplication import naive_square_matrix_product
from multiplication import strassen_square_matrix_product

def get_performance_multiplication():

    data = {'shape': []}
    for i in range(1, FLAGS.max_degree):

        sshape = 2 ** i
        min_max_value = sshape * 2
        a = np.random.randint(
            -min_max_value, min_max_value, size=(sshape, sshape)).tolist()
        b = np.random.randint(
            -min_max_value, min_max_value, size=(sshape, sshape)).tolist()

        data['shape'].append(sshape)
        for algorithm, desc in [
                        ('naive_square_matrix_product', 'naive O(n^3)'),
                        ('strassen_square_matrix_product', 'Strassen O(n^2.81)'),
                        ]:
            duration = timeit.Timer(
                algorithm + '({}, {})'.format(a, b),
                """from __main__ import {}""".format(algorithm)
                ).timeit(number=1)
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
    results = pd.read_csv(FLAGS.results_file, index_col='shape')

    # plot chart
    fig, ax = plt.subplots(1)
    for name in results.columns:
        (results[name]).plot(ax=ax)

    ax.set_title('Comparison of matrix multiplication algorithms')
    ax.set_ylabel('time duration, s')
    ax.set_xlabel('shape of square matrix')
    ax.legend()

    plt.show()

def main():

    if FLAGS.force or not os.path.isfile(FLAGS.results_file):
        if not os.path.isdir(os.path.dirname(FLAGS.results_file)):
            os.makedirs(os.path.dirname(FLAGS.results_file))

        data = get_performance_multiplication()
        dataframe = pd.DataFrame(data).set_index('shape')
        dataframe.to_csv(FLAGS.results_file)
        print('Data saved to "{}" file'.format(FLAGS.results_file))

    plot_chart()

if __name__ in "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--max_degree', type=int, default=10)
    parser.add_argument(
        '--results_file',
        type=str,
        default=os.path.join(tempfile.gettempdir(),
                             'fun-with-algorithms',
                             'matrix_multiplication.csv'),
        help='File with results')

    FLAGS, unparsed = parser.parse_known_args()
    main()
