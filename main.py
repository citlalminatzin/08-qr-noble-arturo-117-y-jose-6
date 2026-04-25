#!/usr/bin/env python

import math
from eigenvalues import eigenvals, eigenvals_tol
from linearsolve import solve
from gram_schmidt import matrix_to_str

def resolver_polinomio_caracteristico_2x2(A: list[list[float]]) -> tuple[float, float]:
    """
    Resuelve el polinomio característico para una matriz 2x2 de la forma:
    lambda^2 - tr(A)*lambda + det(A) = 0
    """
    traza = A[0][0] + A[1][1]
    determinante = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
    
    # Fórmula general para la ecuación cuadrática ax^2 + bx + c = 0
    # a = 1, b = -traza, c = determinante
    discriminante = (traza**2) - (4 * determinante)
    
    if discriminante < 0:
        raise ValueError("Los eigenvalores son complejos, este método solo maneja reales.")
        
    lambda_1 = (traza + math.sqrt(discriminante)) / 2
    lambda_2 = (traza - math.sqrt(discriminante)) / 2
    
    return lambda_1, lambda_2

def main():
    # Matriz A definida en el Ejercicio 1 de la práctica
    A_ejercicio = [
        [5.0, -2.0],
        [-2.0, 8.0]
    ]

    print("==================================================")
    print(" EJERCICIO 1: Método del polinomio característico ")
    print("==================================================")
    print("Matriz A:")
    print(matrix_to_str(A_ejercicio))
    print("-" * 50)
    
    try:
        l1, l2 = resolver_polinomio_caracteristico_2x2(A_ejercicio)
        print("Eigenvalores calculados analíticamente (Polinomio Característico):")
        print(f" λ1: {l1:.6f}")
        print(f" λ2: {l2:.6f}")
    except Exception as e:
        print(f"Error en Ejercicio 1: {e}")


    print("\n==================================================")
    print(" EJERCICIO 2: El Método QR Simple                 ")
    print("==================================================")
    # El ejercicio 2 pide probar con 10 iteraciones
    n_iteraciones_ej2 = 10
    print(f"Aplicando algoritmo QR con {n_iteraciones_ej2} iteraciones...")
    print("-" * 50)
    
    try:
        # eigenvals ya extrae y retorna la diagonal de A_k
        resultados_qr = eigenvals(A_ejercicio, n=n_iteraciones_ej2)
        
        print(f"Eigenvalores tras {n_iteraciones_ej2} iteraciones (Método QR):")
        for i, val in enumerate(resultados_qr):
            print(f" λ{i+1}: {val:.6f}")
            
    except Exception as e:
        print(f"Error en Ejercicio 2 (QR): {e}")

    print("\n==================================================")
    print(" PRUEBA EXTRA: Resolución de Sistema Ax = b       ")
    print("==================================================")
    A_sys = [
        [1.0, 1.0],
        [1.0, -1.0]
    ]
    b = [2.0, 0.0]
    print("Matriz A_sys:")
    print(matrix_to_str(A_sys))
    print(f"Vector b: {b}")

    try:
        x = solve(A_sys, b)
        print(f"\nSolución encontrada x: {x}")
    except Exception as e:
        print(f"Error en sistema lineal: {e}")

    print("\n==================================================")
    print(" EJERCICIO 3: El Método QR con Tolerancia         ")
    print("==================================================")
    max_iteraciones = 1000
    tolerancia = 1e-10
    
    try:
        resultados_qr_tol, iteraciones_reales = eigenvals_tol(A_ejercicio, max_iter=max_iteraciones, tol=tolerancia)
        print(f"Convergencia alcanzada en la iteración: {iteraciones_reales}")
        print("Eigenvalores calculados:")
        for i, val in enumerate(resultados_qr_tol):
            print(f" λ{i+1}: {val:.10f}")
    except Exception as e:
        print(f"Error en Ejercicio 3: {e}")

if __name__ == "__main__":
    main()
