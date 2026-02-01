import numpy as np
import pytest

from src.series import gregory_series, pi_gregory_series


@pytest.mark.parametrize(
    "x, n",
    [(x, n) for x in np.linspace(-1, 1, num=10) for n in [512, 1024, 2048]],
)
def test_gregory_series(x, n):
    series = gregory_series(x, n)
    y = np.arctan(x)
    y_pred = np.sum(series)
    np.testing.assert_allclose(y, y_pred, atol=1e-3, rtol=1e-3)


@pytest.mark.parametrize(
    "n",
    [512, 1024, 2048],
)
def test_pi_gregory_series_sum(n):
    series = pi_gregory_series(n)
    np.testing.assert_allclose(np.pi, np.sum(series), atol=1e-3, rtol=1e-3)


@pytest.mark.parametrize(
    "n, expected_sum",
    [
        (1, 4.0),
        (2, 2.666),
        (3, 3.4666),
        (4, 2.895238),
        (5, 3.339682),
    ],
)
def test_pi_gregory_series_partial_sum(n, expected_sum):
    series = pi_gregory_series(n)
    np.testing.assert_allclose(expected_sum, np.sum(series), atol=1e-3, rtol=1e-3)
