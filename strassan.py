def strassen(A, B):
    n = len(A)

    # Base case: 1x1 matrix
    if n == 1:
        return A[0][0] * B[0][0]

    # Divide the matrices into 4 sub-matrices
    mid = n // 2
    A11, A12, A21, A22 = [x[:mid] for x in A[:mid]], [x[mid:] for x in A[:mid]], [x[:mid] for x in A[mid:]], [x[mid:] for x in A[mid:]]
    B11, B12, B21, B22 = [x[:mid] for x in B[:mid]], [x[mid:] for x in B[:mid]], [x[:mid] for x in B[mid:]], [x[mid:] for x in B[mid:]]

    # Compute the 7 products using Strassen's formula
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))

    # Combine the products to get the final result
    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = sub(add(M1, M3), M2)

    # Combine the sub-matrices to get the final result
    C = [[C11[i][j] for j in range(mid)] + [C12[i][j] for j in range(mid)] for i in range(mid)] + [[C21[i][j] for j in range(mid)] + [C22[i][j] for j in range(mid)] for i in range(mid)]

    return C

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Example usage
A = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2]]
B = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2]]

C = strassen(A, B)
print("Result:")
for row in C:
    print(row)