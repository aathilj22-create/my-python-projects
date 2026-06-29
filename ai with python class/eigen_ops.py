import numpy as np

# Step 1: Define a 2x2 Matrix
matrix_A = np.array([
    [1, 2],
    [2, 4]
])

print("--- ORIGINAL MATRIX (A) ---")
print(matrix_A)

# Step 2: Calculate Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix_A)

# Step 3: Print the Results
print("\n1. EIGENVALUES:")
print(eigenvalues)

print("\n2. EIGENVECTORS:")
print(eigenvectors)

# Step 4: Keep terminal open
input("\nPress Enter to exit...")