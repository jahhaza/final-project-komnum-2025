import numpy as np

def lagrange_interpolation(x_values, y_values, x_target):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x_target - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return round(result, 2)

x_points = [6, 9, 12, 15]
y_points = [234, 960, 2280, 4356]

x_target = 11

estimated_value = lagrange_interpolation(x_points, y_points, x_target)

print(f"Taksiran nilai f(11) adalah: {estimated_value}")
