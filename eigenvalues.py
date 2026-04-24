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
