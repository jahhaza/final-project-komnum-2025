import sympy as sp

class NewtonRaphsonSolver:
    def __init__(self, func_expr, x0, x_true, max_iter=3):
        self.x = sp.symbols('x')
        self.f = func_expr
        self.df = sp.diff(self.f, self.x)
        self.x0 = x0
        self.x_true = x_true
        self.max_iter = max_iter

    def evaluate(self, expr, val):
        return float(expr.subs(self.x, val))

    def solve(self):
        print(f"{'Iter':<5} {'x_n':<10} {'Et (%)':<10} {'Ea (%)':<10}")
        x_old = self.x0
        for i in range(1, self.max_iter + 1):
            fx = self.evaluate(self.f, x_old)
            dfx = self.evaluate(self.df, x_old)

            x_new = x_old - fx / dfx
            Et = abs((self.x_true - x_new) / self.x_true) * 100
            Ea = abs((x_new - x_old) / x_new) * 100 if i > 1 else 0

            print(f"{i:<5} {x_new:.2f}     {Et:.2f}      {Ea:.2f}")
            x_old = x_new

f_expr = sp.sympify("x**3 + 6*x**2 - 19*x - 84")
x0 = 1
x_true = -3

solver = NewtonRaphsonSolver(f_expr, x0, x_true)
solver.solve()
