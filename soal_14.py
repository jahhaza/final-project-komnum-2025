import numpy as np

def g(x):
    return round((-6*x**2 + 19*x + 84)**(1/3), 2)

def fixed_point_iteration(x0, x_true, max_iter=5):
    results = []
    for i in range(max_iter):
        x1 = g(x0)
        Et = round(abs(x_true - x1), 2)
        Ea = round(abs((x1 - x0) / x1) * 100, 2) if x1 != 0 else None
        results.append({
            'iterasi': i + 1,
            'x': x1,
            'Et': Et,
            'Ea': Ea
        })
        x0 = x1
    return results

x0 = 5
x_true = 4  

hasil_iterasi = fixed_point_iteration(x0, x_true)

for hasil in hasil_iterasi:
    print(f"Iterasi {hasil['iterasi']}: x = {hasil['x']}, Et = {hasil['Et']}, Ea = {hasil['Ea']}%")
