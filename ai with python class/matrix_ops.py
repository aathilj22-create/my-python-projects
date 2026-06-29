import numpy as np

# Defining a 2x2 Matrix
matrix_A = np.array([
    [1, 2],
    [3, 4]
])

print("--- ORIGINAL MATRIX (A) ---")
print(matrix_A)

# 1. Matrix Transpose
transpose_result = np.transpose(matrix_A)
print("\n1. TRANSPOSE MATRIX (A Transpose):")
print(transpose_result)

# 2. Matrix Determinant
determinant_result = np.linalg.det(matrix_A)
print("\n2. DETERMINANT OF MATRIX (det(A)):")
print(round(determinant_result))

# Keeping the terminal open
input("\nPress Enter to exit...")