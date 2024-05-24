"""
Código extraído de "Métodos numéricos usando Python con aplicaciones a la Ingeniería Química"
por Juan Carlos Jiménez Bedolla (Universidad Nacional Autónoma de México Facultad de Química) (2022)
"""
import numpy as np

def gauss_seidel(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(A)
    x = np.zeros_like(b, dtype=np.double)
    
    for k in range(max_iterations):
        x_old = x.copy()
        
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (b[i] - s1 - s2) / A[i, i]
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
            return x
    
    raise Exception("El método Gauss-Seidel no converge")
