import numpy as np
from sympy import symbols, diff, lambdify

def trapezoidal_composite(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    area = h * (0.5 * y[0] + sum(y[1:n]) + 0.5 * y[n])
    return round(area, 2)

def trapezoidal_composite_error(f_sym, a, b, n):
    x = symbols('x')
    f2 = diff(f_sym, x, 2)
    f2_func = lambdify(x, f2)

    xs = np.linspace(a, b, 1000)
    max_f2 = max(abs(f2_func(xs)))

    h = (b - a) / n
    error = ((b - a) * h**2 / 12) * max_f2
    return round(error, 2)

x = symbols('x')
f_sym = 3*x**5 - 8*x**4
f_num = lambdify(x, f_sym)

a = 4
b = 16
n = 10  

luas = trapezoidal_composite(f_num, a, b, n)
error = trapezoidal_composite_error(f_sym, a, b, n)

print(f"Luas aproksimasi (Trapesium Segmen Berganda) = {luas}")
print(f"Estimasi error                              = {error}")
