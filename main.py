#!/usr/bin/env python

from eigenvalues import eigenvals
from linearsolve import solve
from gram_schmidt import matrix_to_str

def main():
    # Definimos una matriz de prueba (2x2)
    # Sus eigenvalores reales son aproximadamente 5.0 y 2.0
    A = [
        [4.0, 2.0],
        [1.0, 3.0]
    ]

    print("--- Cálculo de Eigenvalores ---")
    print("Matriz original A:")
    print(matrix_to_str(A))
    print("-" * 30)

    # Ejecutamos el algoritmo
    n_iteraciones = 100
    try:
        resultados = eigenvals(A, n=n_iteraciones)
        
        print(f"Eigenvalores tras {n_iteraciones} iteraciones:")
        for i, val in enumerate(resultados):
            print(f" λ{i+1}: {val:.6f}")
            
    except Exception as e:
        print(f"Error en eigenvalores: {e}")

    print("\n" + "="*40 + "\n")

    # --- 2: RESOLUCIÓN DE SISTEMA Ax = b ---
    # Sistema:
    #  1x + 1y = 2
    #  1x - 1y = 0
    # Solución esperada: x=1, y=1
    A_sys = [
        [1.0, 1.0],
        [1.0, -1.0]
    ]
    b = [2.0, 0.0]
    print("RESOLUCIÓN DE SISTEMA Ax = b ===")
    print("Matriz A:")
    print(matrix_to_str(A_sys))
    print(f"Vector b: {b}")

    try:
        x = solve(A_sys, b)
        print(f"\nSolución encontrada x: {x}")
    except Exception as e:
        print(f"Error en sistema lineal: {e}")

if __name__ == "__main__":
    main()
