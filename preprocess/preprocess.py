__all__ = [
    'split_train_test'
]

import typing as tp
import numpy as np
import pandas as pd

DF = pd.DataFrame


def split_train_test(data: DF, test_ratio: float, random_state: tp.Optional[int] = None):
    """Slipt data into train and test sets.
    
    :param data: Data to be split into two sets.
    :type data: ``pandas.DataFrame``
    :param test_ratio: Proportion of data separated for test set (must be between 0 and 1).
    :type test_ratio: ``float``
    :param random_state: If given, applies the same shuffle across multiple calls.
    :type random_state: ``int``
    :return: ``(train_set, test_set)`` where:
        * train_set: training samples
        * test_set: testing samples
    :rtype:  ``(pandas.DataFrame, pandas.DataFrame)``
    """
    if random_state:
        np.random.seed(random_state)
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
