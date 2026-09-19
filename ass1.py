import numpy as np

# Square matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10]
])

print("Original Matrix:")
print(A)


# ---------------- QR Decomposition ----------------
Q, R = np.linalg.qr(A)

print("\nQ Matrix:")
print(Q)

print("\nR Matrix:")
print(R)

print("\nCheck Q @ R:")
print(Q @ R)


# ---------------- SVD ----------------
U, S, VT = np.linalg.svd(A)

print("\nU Matrix:")
print(U)

print("\nSingular Values:")
print(S)

print("\nVT Matrix:")
print(VT)

# Convert S into a diagonal matrix
S_matrix = np.diag(S)

print("\nS Matrix:")
print(S_matrix)

print("\nCheck U @ S @ VT:")
print(U @ S_matrix @ VT)


# ---------------- QR using list ----------------
qr_list = [Q, R]

print("\nQR as a List:")
print(qr_list)