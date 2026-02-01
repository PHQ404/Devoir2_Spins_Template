import numpy as np


def estimate_ground_state_ratio(
    energies: np.ndarray, spin_numbers: np.ndarray
) -> float:
    """Estimates the ground state ratio of a given system.

    The ground state ratio is given by:

    .. math::
        \frac{E_0}{N}

    where :math:`E_0` is the ground state energy and :math:`N` is the spin number.

    :param energies: The energies of the systems.
    :type energies: np.ndarray
    :param spin_numbers: The spin numbers of the systems.
    :type spin_numbers: np.ndarray
    :return: The ground state ratio.
    :rtype: float
    """
    raise NotImplementedError("This function is not implemented yet.")


def estimate_excitation_gap(
    ground_energies: np.ndarray, excited_energies: np.ndarray
) -> float:
    """Estimates the excitation gap of a given system.

    The excitation gap is given by:

    .. math::
        E_1 - E_0

    where :math:`E_0` is the ground state energy and :math:`E_1` is the excited state energy.

    :param ground_energies: The ground state energies of the systems.
    :type ground_energies: np.ndarray
    :param excited_energies: The excited state energies of the systems.
    :type excited_energies: np.ndarray
    :return: The ground state energy difference.
    :rtype: float
    """
    raise NotImplementedError("This function is not implemented yet.")
