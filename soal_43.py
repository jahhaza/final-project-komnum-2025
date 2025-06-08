import numpy as np
from sympy import symbols, diff, integrate, lambdify

def simpson_one_third(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Jumlah segmen (n) harus genap untuk metode Simpson 1/3.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    area = h/3 * (y[0] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2]) + y[n])
    return round(area, 2)

def simpson_error(f_sym, a, b, n, approx_value):
    x = symbols('x')
    f4 = diff(f_sym, x, 4)
    f4_func = lambdify(x, f4)
    
    xs = np.linspace(a, b, 1000)
    f4_vals = f4_func(xs)
    max_f4 = np.max(np.abs(f4_vals))

    h = (b - a) / n
    error = (b - a) * h**4 * max_f4 / 180
    return round(error, 2)

x = symbols('x')
f_sym = -4 + 7*x**2
f_num = lambdify(x, f_sym)

a = 0
b = 12
n = 6 

luas = simpson_one_third(f_num, a, b, n)
error = simpson_error(f_sym, a, b, n, luas)

print(f"Luas aproksimasi (Simpson 1/3) = {luas}")
print(f"Estimasi error                 = {error}")
