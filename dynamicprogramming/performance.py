# coding: utf-8


from __future__ import print_function

import os
import timeit

import argparse
import tempfile

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('seaborn')

import pandas as pd

from cut_rod import cut_rod
from cut_rod import memoized_cut_rod
from cut_rod import bottom_up_cut_rod

def get_performance_data():

    skip_algorithm_list = []
    data = {'numbers': []}

    max_num = 2 ** (FLAGS.max_degree + 1)

    for i in range(1, FLAGS.max_degree + 1):

        n = 2 ** i
        a = np.random.randint(0, max_num, size=(n)).tolist()

        data['numbers'].append(n)
        for algorithm, desc in [('cut_rod', 'simple'),
                                ('memoized_cut_rod', 'memoization'),
                                ('bottom_up_cut_rod', 'bottom up')
                               ]:
            # skip slow algorithms and set NaN
            if algorithm in skip_algorithm_list:
                duration = float('NaN')
            else:
                duration = timeit.Timer(
                    algorithm + '({}, {})'.format(a, n),
                    """from __main__ import {}""".format(algorithm)
                    ).timeit(number=100)
                if desc not in data:
                    data[desc] = []
                # if algorithm work more than max_duration_time
                # add it to skip_algorithm_list
                if duration > FLAGS.max_duration_time:
                    skip_algorithm_list.append(algorithm)

            data[desc].append(duration)

    return data

def read_df():
    """ read results file and return dataframe """
    # check results file
    if not os.path.isfile(FLAGS.results_file):
        raise IOError("No such file '{}'".format(FLAGS.results_file))
    # read DataFrame
    return pd.read_csv(FLAGS.results_file, index_col='numbers')

def plot_chart():
    """ Read result file and plot chart """
    results = read_df()
    # plot chart
    fig, (ax1, ax2) = plt.subplots(2)

    for name in results.columns:
        results[name].plot(ax=ax1)

    for name in results.columns:
        (results[name] / results.index).plot(ax=ax2)

    ax1.set_title('Performance of cut rod algorithms (for 100 launch)')
    ax1.set_ylabel('duration, s')
    ax1.set_xscale('log')
    ax2.set_ylabel('duration / length of rod')
    ax2.set_xscale('log')
    ax2.set_yscale('log')

    for ax in (ax1, ax2):
        ax.set_xlabel('length of rod')
        ax.legend()

    plt.show()


def main():
    if FLAGS.force or not os.path.isfile(FLAGS.results_file):
        if not os.path.isdir(os.path.dirname(FLAGS.results_file)):
            # make folders in tmp
            os.makedirs(os.path.dirname(FLAGS.results_file))
        # get data
        data = get_performance_data()
        dataframe = pd.DataFrame(data).set_index('numbers')
        # save it to tmp folder
        dataframe.to_csv(FLAGS.results_file, header=True)
        print('data saved to {} file'.format(FLAGS.results_file))

    plot_chart()


if __name__ in "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--max_degree', type=int, default=8)
    parser.add_argument('--max_duration_time', type=float, default=2.)
    parser.add_argument(
        '--results_file',
        type=str,
        default=os.path.join(tempfile.gettempdir(),
                             'fun-with-algorithms',
                             'cut_rod.csv'),
        help='File with results')

    FLAGS, unparsed = parser.parse_known_args()
    main()
