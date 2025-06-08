import numpy as np

def jacobi_method(A, b, iterations=2):
    n = len(b)
    x_old = np.zeros(n)
    x_new = np.zeros(n)
    
    for it in range(1, iterations+1):
        for i in range(n):
            s = sum(A[i][j] * x_old[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        x_new = np.round(x_new, 2)
        print(f"Iterasi {it}: a0 = {x_new[0]}, a1 = {x_new[1]}, a2 = {x_new[2]}")
        x_old = x_new.copy()

A = np.array([
    [5, 25, 135],
    [25, 135, 775],
    [135, 775, 4659]
], dtype=float)

b = np.array([485, 2785, 16751], dtype=float)

jacobi_method(A, b, iterations=2)
