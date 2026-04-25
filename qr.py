"""
Realiza la factorización QR de una matriz
"""

from gram_schmidt import transpose, dot, proj, normalize, gm

def qr(M: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    """Realiza la factorización QR de una matriz M"""
    
 
    Q_cols = gm(M)
    
    Q = list(map(list, zip(*Q_cols)))
    
    
    Qt = transpose(Q)
    M_cols = transpose(M)
    
    
    R = [[dot(qi, aj) for aj in M_cols] for qi in Qt]
    
    return Q, R
