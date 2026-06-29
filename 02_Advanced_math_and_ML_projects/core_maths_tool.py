import numpy as np
import sympy as sp

def get_matrix_input(name):
    while True:
        try:
            print(f"\n--- Enter elements for Matrix {name} (2x2) ---")
            row1 = input("Enter Row 1 numbers separated by space (e.g., 4 2): ").split()
            row2 = input("Enter Row 2 numbers separated by space (e.g., 1 3): ").split()
            
            # Check if user entered enough elements
            if len(row1) < 2 or len(row2) < 2:
                print("Error: You must enter 2 numbers for each row. Try again.")
                continue
                
            matrix = np.array([[float(row1[0]), float(row1[1])],
                               [float(row2[0]), float(row2[1])]])
            return matrix
        except ValueError:
            print("Invalid input! Please enter numbers only (e.g., 4 or 2.5). Try again.")

def ultimate_math_tool():
    while True:
        print("\n=========================================")
        print("      WELCOME TO ULTIMATE MATH TOOL      ")
        print("=========================================")
        print("1. Matrix Operations")
        print("2. Calculus (Differentiation & Integration)")
        print("3. Exit")
        
        main_choice = input("Choose Category (1, 2, or 3): ")
        
        if main_choice == '1':
            print("\n--- Matrix Operations ---")
            print("1. Matrix Addition")
            print("2. Matrix Transpose")
            print("3. Matrix Determinant")
            print("4. Eigenvalues and Eigenvectors")
            choice = input("Enter your choice (1/2/3/4): ")
            
            if choice == '1':
                A = get_matrix_input("A")
                B = get_matrix_input("B")
                print("\nResult of A + B:\n", np.add(A, B))
            elif choice == '2':
                A = get_matrix_input("A")
                print("\nTranspose of Matrix A:\n", np.transpose(A))
            elif choice == '3':
                A = get_matrix_input("A")
                print("\nDeterminant of Matrix A:", round(np.linalg.det(A), 2))
            elif choice == '4':
                A = get_matrix_input("A")
                vals, vecs = np.linalg.eig(A)
                print("\nEigenvalues:", vals)
                print("\nEigenvectors:\n", vecs)
                
        elif main_choice == '2':
            print("\n--- Calculus Operations ---")
            equation_str = input("Enter equation in terms of x (e.g., x**2 or 2*x): ")
            
            try:
                x = sp.Symbol('x')
                expr = sp.sympify(equation_str)
                
                print("\n1. Differentiation")
                print("2. Integration")
                calc_choice = input("Enter choice (1 or 2): ")
                
                if calc_choice == '1':
                    diff_result = sp.diff(expr, x)
                    print(f"\nDifferentiation of {equation_str} is: {diff_result}")
                elif calc_choice == '2':
                    int_result = sp.integrate(expr, x)
                    print(f"\nIntegration of {equation_str} is: {int_result} + C")
            except Exception:
                print("Invalid equation format! Please check your math expression syntax.")
                
        elif main_choice == '3':
            print("\nThank you for using Ultimate Math Tool! Bye!")
            break
            
        else:
            print("Invalid choice! Try again.")
            
        repeat = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if repeat != 'yes' and repeat != 'y':
            print("\nThank you for using Ultimate Math Tool! Bye!")
            break

if __name__ == "__main__":
    ultimate_math_tool()
    input("\nPress Enter to exit...")