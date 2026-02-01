import scipy.sparse as sparse


class Heisenberg:
    r"""Class defining a 1D spins chain system based on Heisenberg model.

    :param n: The number of spins in the periodic chain.
    :type n: int
    :param j: The coupling constant.
    :type j: float

    :ivar n: The number of spins in the periodic chain.
    :ivar j: The coupling constant.
    :ivar _hamiltonian: The Hamiltonian of the system.
    :ivar _ground_state: The ground state of the system (E0).
    :ivar _excited_state: The excited state of the system (E1).
    """

    def __init__(self, n: int, j: float = 1.0):
        """
        Constructor of the class.

        :param n: The number of spins in the periodic chain.
        :type n: int
        :param j: The coupling constant.
        :type j: float
        """
        self.n = n
        self.j = j
        self._hamiltonian = None
        self._ground_state = None
        self._excited_state = None

    @property
    def hamiltonian(self) -> sparse.spmatrix:
        """
        The Hamiltonian of the system.

        :Note: If the Hamiltonian is not computed yet, it will be computed and stored.

        :return: The Hamiltonian of the system.
        :rtype: sparse.spmatrix
        """
        if self._hamiltonian is None:
            self._hamiltonian = self._build_hamiltonian()
        return self._hamiltonian

    @property
    def ground_state(self) -> float:
        """
        The ground state of the system (E0).

        :Note: If the ground state is not computed yet, it will be computed and stored.

        :return: The ground state of the system.
        :rtype: float
        """
        if self._ground_state is None:
            self._ground_state = self._compute_ground_state()
        return self._ground_state

    @property
    def excited_state(self) -> float:
        """
        The excited state of the system (E1).

        :Note: If the excited state is not computed yet, it will be computed and stored.

        :return: The excited state of the system.
        :rtype: float
        """
        if self._excited_state is None:
            self._excited_state = self._compute_excited_state()
        return self._excited_state

    def _build_hamiltonian(self) -> sparse.spmatrix:
        """
        Build the Hamiltonian of the system.

        :return: The Hamiltonian of the system.
        :rtype: sparse.spmatrix
        """
        raise NotImplementedError("This function is not implemented yet.")

    def _compute_ground_state(self) -> float:
        """
        Compute the ground state of the system.

        :return: The ground state of the system.
        :rtype: float
        """
        raise NotImplementedError("This function is not implemented yet.")

    def _compute_excited_state(self) -> float:
        """
        Compute the excited state of the system.

        :return: The excited state of the system.
        :rtype: float
        """
        raise NotImplementedError("This function is not implemented yet.")
