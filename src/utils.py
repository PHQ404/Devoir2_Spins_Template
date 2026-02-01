import numpy as np
from scipy import sparse


def to_sparse(array: np.ndarray, dtype: np.dtype | None = None) -> sparse.spmatrix:
    """Converts a given array to a sparse matrix.

    :param array: The array to convert.
    :type array: np.ndarray
    :param dtype: The data type of the sparse matrix. If None, the data type of the array is used.
    :type dtype: np.dtype or None
    :return: The sparse matrix.
    :rtype: sparse.spmatrix
    """
    if dtype is None:
        return sparse.csr_array(array)
    else:
        return sparse.csr_array(array, dtype=dtype)


def to_dense(sparse_matrix: sparse.spmatrix) -> np.ndarray:
    """Converts a given sparse matrix to a dense array.

    :param sparse_matrix: The sparse matrix to convert.
    :type sparse_matrix: sparse.spmatrix
    :return: The dense array.
    :rtype: np.ndarray
    """
    return sparse_matrix.toarray()


Sx = to_sparse(np.array([[0, 1], [1, 0]]) / 2)
Sy = to_sparse(np.array([[0, -1], [1, 0]]) / 2)
Sz = to_sparse(np.array([[1, 0], [0, -1]]) / 2)
