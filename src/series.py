import numpy as np


def gregory_series(x: float, n: int) -> np.ndarray:
    r"""Calculates the n terms of the Gregory series for a given x. The returned values
    are each term in the summation.

    The Gregory series is given by:

    .. math::
        \arctan(x) = \sum_{i=0}^{n-1} \frac{(-1)^i}{2i+1} x^{2i+1}

    :param x: The value to calculate the series for.
    :type x: float
    :param n: The number of terms in the series.
    :type n: int
    :return: The Gregory series.
    :rtype: np.ndarray
    """
    indexes = np.arange(n)
    signs = (-1) ** indexes
    denominator = 2 * indexes + 1
    numerator = signs * (x**denominator)
    return numerator / denominator


def pi_gregory_series(n: int) -> np.ndarray:
    r"""Calculates the Gregory series used to calculate pi for a given n.

    This Gregory series is given by:

    .. math::
        \pi = 4 \sum_{i=0}^{n-1} \frac{(-1)^i}{2i+1}

    :param n: The number of terms in the series.
    :type n: int
    :return: The value of pi.
    :rtype: np.ndarray
    """
    return 4 * gregory_series(1, n)
