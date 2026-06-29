import numpy as np

def get_matrix_input(name):
    print(f"\n--- Enter elements for Matrix {name} (2x2) ---")
    row1 = input("Enter Row 1 numbers separated by space (e.g., 4 2): ").split()
    row2 = input("Enter Row 2 numbers separated by space (e.g., 1 3): ").split()
    
    matrix = np.array([[float(row1[0]), float(row1[1])],
                       [float(row2[0]), float(row2[1])]])
    return matrix

def matrix_calculator():
    print("=== WELCOME TO DYNAMIC MATRIX CALCULATOR ===")
    print("1. Matrix Addition")
    print("2. Matrix Transpose")
    print("3. Matrix Determinant")
    print("4. Eigenvalues and Eigenvectors")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
       
        A = get_matrix_input("A")
        B = get_matrix_input("B")
        result = np.add(A, B)
        print("\nResult of A + B:\n", result)
        
    elif choice == '2':
        A = get_matrix_input("A")
        result = np.transpose(A)
        print("\nTranspose of Matrix A:\n", result)
        
    elif choice == '3':
        A = get_matrix_input("A")
        result = np.linalg.det(A)
        print("\nDeterminant of Matrix A:", round(result, 2))
        
    elif choice == '4':
        A = get_matrix_input("A")
        eigenvalues, eigenvectors = np.linalg.eig(A)
        print("\nEigenvalues:", eigenvalues)
        print("\nEigenvectors:\n", eigenvectors)
        
    else:
        print("Invalid choice!")

# Running the calculator
matrix_calculator()

input("\nPress Enter to exit...")