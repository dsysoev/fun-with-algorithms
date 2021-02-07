"""
Implementing performance for basic math operation in python
"""


from time import time
from functools import wraps

import numpy as np
import pandas as pd


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        value = func(*args, **kwargs)
        end_ = int(round(time() * 1000)) - start
        return value, end_

    return _time_it

@measure
def eval_operation(operation, lst0, lst1):
    string = 'for x, y in zip({}, {}): _ = x {} y'.format(lst0, lst1, operation)
    return exec(string)


if __name__ in '__main__':

    operation_list = ['+', '-', '/', '*', '**']

    data = []
    for max_value in [1e3, 1e4]:
        for num_elements in [1e3, 1e4, 1e5]:

            lst = np.random.random_integers(
                -max_value, max_value, size=int(num_elements)).tolist()
            # prevent zero division error
            lst = [x for x in lst if x != 0]
            reversed_lst = list(reversed(lst))

            for operation in operation_list:
                _, evaltime = eval_operation(operation, lst, reversed_lst)

                data.append({
                    'operation': operation,
                    'evaltime': evaltime,
                    'max_value': int(max_value),
                    'num_elements': int(num_elements)
                    })

    df = pd.DataFrame(data)
    print(('evaluation time (ms) for max value in list equal to 10000'
        ' over number of elements in list'))
    print(df[df.max_value == 10000].pivot(
        index='num_elements', columns='operation', values='evaltime'))

    print(('\nevaluation time (ms) for list with length equal to 10000'
        ' over max value in list'))
    print(df[df.num_elements == 10000].pivot(
        index='max_value', columns='operation', values='evaltime'))
