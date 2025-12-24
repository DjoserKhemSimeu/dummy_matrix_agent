"""
Matrix multiplication example with a deliberate bug.
"""

def multiply_matrices(A, B):
    """
    Multiply two matrices A and B.

    BUG (intentional):
    The indices used in the multiplication are incorrect,
    which leads to wrong numerical results.
    """
    m = len(A)
    p = len(B[0])
    C = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(len(B)):  # should be len(A[0])
                # Intentional bug: wrong indices
                total += A[k][i] * B[j][k]
            C[i][j] = total

    return C


def main():
    A = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    B = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]

    print("Matrix A:")
    for row in A:
        print(row)

    print("Matrix B:")
    for row in B:
        print(row)

    result = multiply_matrices(A, B)

    print("Result of A × B (with bug):")
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
