import numpy as np
import pytest

from src.hamiltonian import Heisenberg
from src.utils import to_dense


@pytest.mark.parametrize(
    "n, j, h",
    [
        (
            3,
            j,
            j
            / 4
            * np.array(
                [
                    [3, 0, 0, 0, 0, 0, 0, 0],
                    [0, -1, 2, 0, 2, 0, 0, 0],
                    [0, 2, -1, 0, 2, 0, 0, 0],
                    [0, 0, 0, -1, 0, 2, 2, 0],
                    [0, 2, 2, 0, -1, 0, 0, 0],
                    [0, 0, 0, 2, 0, -1, 2, 0],
                    [0, 0, 0, 2, 0, 2, -1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 3],
                ]
            ),
        )
        for j in [1, 2, 3]
    ],
)
def test_hamiltonian(n, j, h):
    model = Heisenberg(n, j)
    hamiltonian = to_dense(model.hamiltonian)
    np.testing.assert_allclose(hamiltonian, h, atol=1e-4, rtol=1e-4)


@pytest.mark.parametrize(
    "n, j",
    [(n, j) for j in [1, 2, 3] for n in [2, 3, 4]],
)
def test_real_hamiltonian(n, j):
    model = Heisenberg(n, j)
    hamiltonian = to_dense(model.hamiltonian)
    np.testing.assert_allclose(hamiltonian, hamiltonian.conj(), atol=1e-4, rtol=1e-4)
