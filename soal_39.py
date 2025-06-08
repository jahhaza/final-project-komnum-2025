import numpy as np
from sympy import symbols, diff, lambdify

def simpson_38(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("n harus kelipatan 3 untuk metode Simpson 3/8.")
    
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    area = (3 * h / 8) * (y[0] + y[-1] +
                          3 * sum(y[1:-1:1][(np.arange(1, n) % 3 != 0)]) +
                          2 * sum(y[3:-1:3]))
    return round(area, 2)

def simpson_38_error(f_sym, a, b, n):
    x = symbols('x')
    f4 = diff(f_sym, x, 4)  
    f4_func = lambdify(x, f4)

    xs = np.linspace(a, b, 1000)
    max_f4 = max(abs(f4_func(xs)))

    h = (b - a) / n
    error = ((b - a) * h**4 / 80) * max_f4
    return round(error, 2)

x = symbols('x')
f_sym = 3*x**5 - 8*x**4
f_num = lambdify(x, f_sym)

a = 4
b = 16
n = 6  

luas = simpson_38(f_num, a, b, n)
error = simpson_38_error(f_sym, a, b, n)

print(f"Luas aproksimasi (Simpson 3/8) = {luas}")
print(f"Estimasi error                = {error}")
