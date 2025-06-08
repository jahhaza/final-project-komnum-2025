import numpy as np
from sympy import symbols, integrate, lambdify

def riemann_sum(f, a, b, n, method='mid'):
    h = (b - a) / n
    if method == 'left':
        x = np.linspace(a, b - h, n)
    elif method == 'right':
        x = np.linspace(a + h, b, n)
    elif method == 'mid':
        x = np.linspace(a + h/2, b - h/2, n)
    else:
        raise ValueError("Method harus 'left', 'right', atau 'mid'")
    
    y = f(x)
    area = np.sum(y * h)
    return round(area, 2)

def riemann_error(f_sym, a, b, approx_value):
    x = symbols('x')
    exact = integrate(f_sym, (x, a, b))
    error = abs(float(exact) - approx_value)
    return round(error, 2)

x = symbols('x')
f_sym = 3*x**5 - 8*x**4
f_num = lambdify(x, f_sym)

a = 4
b = 16
n = 100 
method = 'mid'  

luas = riemann_sum(f_num, a, b, n, method)
error = riemann_error(f_sym, a, b, luas)

print(f"Luas aproksimasi (Riemann {method}) = {luas}")
print(f"Estimasi error                     = {error}")
