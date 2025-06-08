import numpy as np

def gauss_seidel(coeffs, constants, iterations=2):
    n = len(constants)
    x = np.zeros(n) 
    
    for itr in range(1, iterations + 1):
        x_new = np.copy(x)
        for i in range(n):
            sum1 = sum(coeffs[i][j] * x_new[j] for j in range(i))
            sum2 = sum(coeffs[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (constants[i] - sum1 - sum2) / coeffs[i][i]
        
        x = x_new
        print(f"Iterasi ke-{itr}: a0 = {x[0]:.2f}, a1 = {x[1]:.2f}, a2 = {x[2]:.2f}")

A = np.array([
    [5, 25, 135],
    [25, 135, 775],
    [135, 775, 4659]
], dtype=float)

b = np.array([485, 2785, 16751], dtype=float)

gauss_seidel(A, b, iterations=2)
