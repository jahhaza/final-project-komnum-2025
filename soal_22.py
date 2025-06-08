import sympy as sp

def modified_newton_raphson(f_expr, x0, x_true, max_iter=3):
    x = sp.symbols('x')
    f = f_expr
    f_prime = sp.diff(f, x)
    f_double_prime = sp.diff(f_prime, x)

    print(f"{'Iterasi':<8} {'x':<10} {'f(x)':<10} {'Ea (%)':<10} {'Et (%)':<10}")

    for i in range(1, max_iter + 1):
        fx = f.subs(x, x0).evalf()
        f1x = f_prime.subs(x, x0).evalf()
        f2x = f_double_prime.subs(x, x0).evalf()

        denominator = (f1x ** 2 - fx * f2x)
        if denominator == 0:
            print("Dibagi nol pada iterasi", i)
            break

        x1 = x0 - (fx * f1x) / denominator

        Et = abs((x_true - x1) / x_true) * 100
        Ea = abs((x1 - x0) / x1) * 100 if x1 != 0 else 0

        print(f"{i:<8} {round(x1, 2):<10} {round(f.subs(x, x1), 2):<10} {round(Ea, 2):<10} {round(Et, 2):<10}")

        x0 = x1

f_expr = sp.sympify("12*x**3 - 30*x**2 - 84*x + 48")
x0 = -1
x_true = -2

modified_newton_raphson(f_expr, x0, x_true)
