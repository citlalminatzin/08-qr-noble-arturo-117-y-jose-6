#!/usr/bin/env python

from gram_schmidt import matvec, transpose
from qr import qr

def solve(A: list[list[float]], b: list[float]) -> list[float]:
    """
    Resuelve el sistema Ax = b utilizando la factorización QR.
    """
    m = len(A)
    n = len(A[0])
    
    if len(b) != m:
        raise ValueError("Dimensiones incompatibles entre A y b")
    
    # Factorizamos A en Q (ortogonal) y R (triangular sup.)
    Q, R = qr(A)
    Qt = transpose(Q)
    
    # Calculamos el nuevo vector lado derecho: Q^T * b
    Qt_b = matvec(Qt, b)
    
    # Ajuste de  dimensiones para sistemas sobreterminados 
    Qt_b = Qt_b[:n]
    
    # Sustitución hacia atrás  Rx = Qt_b
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(R[i][j] * x[j] for j in range(i + 1, n))
        if R[i][i] == 0:
            raise ValueError("La matriz es singular y no tiene solución única")
        x[i] = (Qt_b[i] - suma) / R[i][i]
        
    return x

if __name__ == "__main__":
    # Prueba 
    A = [[1.0, 1.0], [1.0, -1.0]]
    b = [2.0, 0.0]
    print("La solución es:", solve(A, b))
