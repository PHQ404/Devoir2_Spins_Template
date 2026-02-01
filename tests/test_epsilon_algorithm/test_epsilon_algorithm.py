import numpy as np
import pytest

from src.epsilon_algorithm import epsilon_algorithm
from src.series import gregory_series, pi_gregory_series


@pytest.mark.parametrize(
    "x, n",
    [
        (x, n)
        for x in np.linspace(0.5, 1, num=10)
        for n in [
            16,
        ]
    ],
)
def test_estimation_of_gregory_series(x, n):
    series = gregory_series(x, n)
    y = np.arctan(x)
    y_pred = epsilon_algorithm(series)
    np.testing.assert_allclose(y, y_pred, atol=1e-3, rtol=1e-3)


@pytest.mark.parametrize(
    "n",
    [8, 16, 32, 512],
)
def test_estimation_of_pi_gregory_series(n):
    series = pi_gregory_series(n)
    y_pred = epsilon_algorithm(series)
    np.testing.assert_allclose(np.pi, y_pred, atol=1e-3, rtol=1e-3)
