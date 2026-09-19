import numpy as np

# Define two 3x3 matrices
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# i) Inverse of Matrix A
A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

print("\nNew Matrix A:")
print(A)

A_inverse = np.linalg.inv(A)

print("\nInverse of Matrix A:")
print(A_inverse)

# ii) Determinant of Matrix B
det_B = np.linalg.det(B)

print("\nDeterminant of Matrix B:")
print(det_B)

# iii) A * A^-1
result = A @ np.linalg.inv(A)

print("\nA × A^-1:")
print(np.round(result,10))