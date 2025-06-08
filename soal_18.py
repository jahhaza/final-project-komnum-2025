import numpy as np

def jacobi_method(A, b, x0, max_iter=2):
    n = len(b)
    x = x0.copy()

    print("Iterasi ke-0:", [round(float(val), 2) for val in x])

    for k in range(1, max_iter + 1):
        x_new = np.zeros_like(x)

        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        x = x_new.copy()
        print(f"Iterasi ke-{k}:", [round(float(val), 2) for val in x])

A = np.array([
    [2, -3, -4],
    [-3, 9, -2],
    [-5, -1, 3]
], dtype=float)

b = np.array([-44, 78, 21], dtype=float)

x0 = np.zeros(3)

jacobi_method(A, b, x0, max_iter=2)
