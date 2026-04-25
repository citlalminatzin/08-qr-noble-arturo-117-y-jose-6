#!/usr/bin/env python

from qr import qr
from gram_schmidt import matmul

def eigenvals(A: list[list[float]], n: int = 100, tolerance = 1e-10) -> list[float]:
    """
    Realiza n iteraciones del algoritmo QR para calcular 
    los eigenvalores de A.
    """
    # Inicializamos A_k con la matriz original
    A_k = A
    
    for _ in range(n):
       #Descomposición de qr en matriz
        Q, R = qr(A_k)
        
       # Nueva matriz
        A_next = matmul(R, Q)
        
        # comparación A_k con A_next.
        
        A_k = A_next
        
    # Los eigenvalores se encuentran en la diagonal de la matriz resultante
    eigenvalues = [A_k[i][i] for i in range(len(A_k))]
    
    return eigenvalues

def eigenvals_tol(A: list[list[float]], max_iter: int, tol: float) -> tuple[list[float], int]:
    """
    Algoritmo QR con criterio de paro por tolerancia (Ejercicio 3).
    Se detiene si los valores fuera de la diagonal son menores a 'tol' 
    o si se alcanza 'max_iter'.
    """
    A_k = A
    dimension = len(A)
    
    for k in range(max_iter):
        Q, R = qr(A_k)
        A_k = matmul(R, Q)
        
        # Encontrar el valor máximo fuera de la diagonal
        max_fuera_diagonal = 0.0
        for i in range(dimension):
            for j in range(dimension):
                if i != j:
                    if abs(A_k[i][j]) > max_fuera_diagonal:
                        max_fuera_diagonal = abs(A_k[i][j])
                        
        # Criterio de paro
        if max_fuera_diagonal < tol:
            # Retornamos los eigenvalores y la iteración en la que convergió
            return [A_k[i][i] for i in range(dimension)], k + 1
            
    # Si termina el ciclo for, se alcanzó max_iter sin cumplir la tolerancia
    return [A_k[i][i] for i in range(dimension)], max_iter