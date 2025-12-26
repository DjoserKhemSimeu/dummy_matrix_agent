def multiply_matrices(A, B):
    m = len(A)
    p = len(B[0])
    C = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(len(A[0])):  # Corrected: len(A[0])
                total += A[k][i] * B[j][k]
            C[i][j] = total

    return C