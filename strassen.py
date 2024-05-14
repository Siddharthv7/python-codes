def strassen_2x2_recursive(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        a11, a12, a21, a22 = split_matrix(A)
        b11, b12, b21, b22 = split_matrix(B)
        # Calculate the following values recursively
        p1 = strassen_2x2_recursive(add_matrices(a11, a22), add_matrices(b11, b22))
        p2 = strassen_2x2_recursive(add_matrices(a21, a22), b11)
        p3 = strassen_2x2_recursive(a11, subtract_matrices(b12, b22))
        p4 = strassen_2x2_recursive(a22, subtract_matrices(b21, b11))
        p5 = strassen_2x2_recursive(add_matrices(a11, a12), b22)
        p6 = strassen_2x2_recursive(subtract_matrices(a21, a11), add_matrices(b11, b12))
        p7 = strassen_2x2_recursive(subtract_matrices(a12, a22), add_matrices(b21, b22))
        # Combine the results into a 2x2 matrix
        c11 = subtract_matrices(add_matrices(add_matrices(p1, p4), p7), p5)
        c12 = add_matrices(p3, p5)
        c21 = add_matrices(p2, p4)
        c22 = subtract_matrices(add_matrices(add_matrices(p1, p3), p6), p2)
        C = [[0, 0], [0, 0]]
        for i in range(n // 2):
            for j in range(n // 2):
                C[i][j] = c11[i][j]
                C[i][j + n // 2] = c12[i][j]
                C[i + n // 2][j] = c21[i][j]
                C[i + n // 2][j + n // 2] = c22[i][j]
        return C

def split_matrix(A):
    n = len(A)
    m = n // 2
    a11 = [[0] * m for i in range(m)]
    a12 = [[0] * m for i in range(m)]
    a21 = [[0] * m for i in range(m)]
    a22 = [[0] * m for i in range(m)]
    for i in range(m):
        for j in range(m):
            a11[i][j] = A[i][j]
            a12[i][j] = A[i][j + m]
            a21[i][j] = A[i + m][j]
            a22[i][j] = A[i + m][j + m]
    return a11, a12, a21, a22

def add_matrices(A, B):
    n = len(A)
    C = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtract_matrices(A, B):
    n = len(A)
    C = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

a = [[12, 1], [23, 80]]
b = [[56, 14], [90, 18]]
print(strassen_2x2_recursive(a, b))
