import numpy as np

def f(x):
    return x**3 + 6*x**2 - 19*x - 84

def secant_method(x0, x1, x_true, max_iter=3):
    results = []
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            print("Error: Division by zero")
            break

        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        x2 = round(x2, 2)
        
        Et = round(abs(x_true - x2), 2)
        Ea = round(abs((x2 - x1) / x2) * 100, 2) if x2 != 0 else None
        
        results.append({
            'iterasi': i + 1,
            'x_n': x2,
            'Et': Et,
            'Ea': Ea
        })
        
        x0, x1 = x1, x2

    return results

x0 = -4
x1 = 3
x_true = -3

hasil_iterasi = secant_method(x0, x1, x_true)

for hasil in hasil_iterasi:
    print(f"Iterasi {hasil['iterasi']}: x = {hasil['x_n']}, Et = {hasil['Et']}, Ea = {hasil['Ea']}%")
