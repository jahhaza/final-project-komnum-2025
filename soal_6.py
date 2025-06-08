import numpy as np

def g(x):
    return (x**3 + 6*x**2 - 84) / 19

def fixed_point_iteration(x0, max_iter=5):
    print(f"{'Iter':<5} {'x_n':<10} {'x_(n+1)':<10} {'|Ea| (%)':<10}")
    for i in range(1, max_iter + 1):
        x1 = g(x0)
        if i == 1:
            ea = None
        else:
            ea = abs((x1 - x0) / x1) * 100
        print(f"{i:<5} {round(x0, 4):<10} {round(x1, 4):<10} {'' if ea is None else round(ea, 4)}")
        x0 = x1

fixed_point_iteration(3)
