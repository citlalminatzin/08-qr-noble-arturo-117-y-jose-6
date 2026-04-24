#!/usr/bin/env python

from qr import qr
from gram_schmidt import matmul

def eigenvals(A:list[list[float]], n:int = 100, tolerance = 1e-10)->list[float]:
    """
    Realiza n iteraciones del algoritmo QR para calcular 
    los eigenvalores de A

    Devuelve la estimación de los eigenvalores
    """
    A_k = A
  
    for _ in range(n):
     # 1. Descomposición QR de la matriz actual
      Q, R = qr(A_k)
        
        # 2. Nueva matriz: multiplicar R y Q en orden inverso
      A_next = matmul(R, Q)

 eigenvalues = [A_k[i][i] for i in range(len(A_k))]
    
    return eigenvalues
