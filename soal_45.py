import numpy as np

def f(x):
    return 4 * x**4 - 12 * x**2

class HeunSolver:
    def __init__(self, func, x0, y0, h, xn):
        self.func = func
        self.x0 = x0
        self.y0 = y0
        self.h = h
        self.xn = xn

    def solve(self):
        x_values = [self.x0]
        y_values = [self.y0]
        x = self.x0
        y = self.y0

        while x < self.xn:
            f1 = self.func(x)
            y_predict = y + self.h * f1
            f2 = self.func(x + self.h)
            y = y + (self.h / 2) * (f1 + f2)
            x = x + self.h
            x_values.append(round(x, 2))
            y_values.append(round(y, 2))

        return x_values, y_values

    def exact_integral(self):
        def F(x):
            return (4/5)*x**5 - 4*x**3
        return round(F(self.xn) - F(self.x0), 2)

    def error(self):
        _, approx = self.solve()
        exact = self.exact_integral()
        error = round(abs(approx[-1] - exact), 2)
        return error

heun = HeunSolver(f, x0=2, y0=0, h=3, xn=11)
x_vals, y_vals = heun.solve()
exact_val = heun.exact_integral()
error_val = heun.error()

print("Hasil Metode Heun:")
for xi, yi in zip(x_vals, y_vals):
    print(f"x = {xi}, y = {yi}")

print(f"\nNilai integral eksak: {exact_val}")
print(f"Error: {error_val}")
