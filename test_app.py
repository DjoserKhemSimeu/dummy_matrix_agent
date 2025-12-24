import pytest
from app import multiply_matrices


def test_main_matrix_multiplication():
    """
    Tests the correctness of the matrix multiplication
    implemented in app.py.

    This test is expected to FAIL until the bug
    in multiply_matrices is fixed.
    """

    A = [
        [1, 2],
        [3, 4]
    ]
    B = [
        [5, 6],
        [7, 8]
    ]

    # Mathematically correct result
    expected = [
        [19, 22],
        [43, 50]
    ]

    result = multiply_matrices(A, B)

    assert result == expected
