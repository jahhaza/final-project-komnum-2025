import numpy as np

def f(x):
    return x**3 + 6*x**2 - 19*x - 84

def df(x):
    return 3*x**2 + 12*x - 19

def newton_raphson_simple(x0, true_root=3.00, max_iter=20):
    xn = x0
    iterasi = 1
    print("Iterasi\t x_n\t\t f(x_n)")
    while iterasi <= max_iter:
        fxn = f(xn)
        dfxn = df(xn)
        xn_next = xn - fxn / dfxn
        xn_rounded = round(xn_next, 2)
        print(f"{iterasi}\t {xn_rounded:.2f}\t {round(f(xn_rounded), 2)}")
        if xn_rounded == true_root:
            break
        xn = xn_next
        iterasi += 1

newton_raphson_simple(-4, 3)

