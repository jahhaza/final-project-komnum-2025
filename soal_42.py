import numpy as np
from sympy import symbols, integrate, lambdify

def gauss_2_point(f, a, b):
    xi = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
    wi = np.array([1, 1])
    
    t = ((b - a) / 2) * xi + (a + b) / 2
    result = (b - a) / 2 * np.sum(wi * f(t))
    return round(result, 2)

def gauss_error(f_sym, a, b, approx_value):
    x = symbols('x')
    exact = integrate(f_sym, (x, a, b))
    error = abs(float(exact) - approx_value)
    return round(error, 2)

x = symbols('x')
f_sym = 3*x**5 - 8*x**4
f_num = lambdify(x, f_sym)

a = 4
b = 16

luas = gauss_2_point(f_num, a, b)
error = gauss_error(f_sym, a, b, luas)

print(f"Luas aproksimasi (Gauss 2 titik) = {luas}")
print(f"Estimasi error                  = {error}")
