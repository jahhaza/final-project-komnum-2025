import numpy as np
from math import factorial

x_vals = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27])
y_vals = np.array([-741, 555, 30237, 31752, 88776, 436366, 897104, 1483298,
                   2459808, 3709707, 5264520, 7143126, 9363099, 11946701, 14751562, 13620771])

def difference_table(y):
    n = len(y)
    diff_table = [y.copy()]
    for i in range(1, n):
        diff = [round(diff_table[i - 1][j + 1] - diff_table[i - 1][j], 2) for j in range(n - i)]
        diff_table.append(diff)
    return diff_table

# Newton-Gregory Forward
def newton_forward(x_vals, y_vals, x, x0_index):
    h = x_vals[1] - x_vals[0]
    u = (x - x_vals[x0_index]) / h
    diff_table = difference_table(y_vals)

    n_terms = len(x_vals) - x0_index  
    result = y_vals[x0_index]
    for i in range(1, n_terms):
        u_product = 1
        for j in range(i):
            u_product *= (u - j)
        term = (u_product * diff_table[i][x0_index]) / factorial(i)
        result += term

    return round(result, 2)

# Newton-Gregory Backward
def newton_backward(x_vals, y_vals, x, x0_index):
    h = x_vals[1] - x_vals[0]
    u = (x - x_vals[x0_index]) / h
    diff_table = difference_table(y_vals)

    n_terms = x0_index + 1 
    result = y_vals[x0_index]
    for i in range(1, n_terms):
        u_product = 1
        for j in range(i):
            u_product *= (u + j)
        term = (u_product * diff_table[i][x0_index - i]) / factorial(i)
        result += term

    return round(result, 2)

# Stirling 
def stirling(x_vals, y_vals, x, x0_index):
    h = x_vals[1] - x_vals[0]
    u = (x - x_vals[x0_index]) / h
    diff_table = difference_table(y_vals)

    result = y_vals[x0_index]
    for i in range(1, min(x0_index + 1, len(x_vals) - x0_index)):
        if i >= len(diff_table):
            break
        if i % 2 == 0:
            k = i // 2
            term = ((u**2 - (k - 1)**2) * diff_table[2 * k][x0_index - k]) / factorial(2 * k)
        else:
            k = (i - 1) // 2
            term = (u * diff_table[2 * k + 1][x0_index - k]) / factorial(2 * k + 1)
        result += term
    return round(result, 2)

# Bessel
def bessel(x_vals, y_vals, x, x0_index):
    h = x_vals[1] - x_vals[0]
    u = (x - x_vals[x0_index]) / h
    diff_table = difference_table(y_vals)

    if x0_index >= len(diff_table[1]) or x0_index - 1 < 0:
        return None

    f0 = y_vals[x0_index]
    f1 = y_vals[x0_index + 1]
    delta1 = diff_table[1][x0_index]
    delta2 = diff_table[2][x0_index]
    delta2_1 = diff_table[2][x0_index - 1]
    delta3 = diff_table[3][x0_index - 1]

    result = (f0 + f1) / 2
    result += (u - 0.5) * delta1
    result += ((u - 0.5)**2 - 1/4) * (delta2 + delta2_1) / 4
    result += ((u - 0.5)**3 - (u - 0.5)) * delta3 / 6

    return round(result, 2)

def error(true_value, interpolated):
    return round(abs(true_value - interpolated), 2)

true_val = 897104
true_val_27 = 436366

print("Soal 25 - Newton Forward (x=16, X0=15):")
res25 = newton_forward(x_vals, y_vals, 16, 5)
print("  f(x) =", res25, "| Et =", error(true_val, res25))

print("Soal 26 - Newton Backward (x=16, X0=15):")
res26 = newton_backward(x_vals, y_vals, 16, 5)
print("  f(x) =", res26, "| Et =", error(true_val, res26))

print("Soal 27 - Stirling (x=14, X0=15):")
res27 = stirling(x_vals, y_vals, 14, 5)
print("  f(x) =", res27, "| Et =", error(true_val_27, res27))

print("Soal 28 - Stirling (x=16, X0=15):")
res28 = stirling(x_vals, y_vals, 16, 5)
print("  f(x) =", res28, "| Et =", error(true_val, res28))

print("Soal 29 - Bessel (x=16, X0=15):")
res29 = bessel(x_vals, y_vals, 16, 5)
print("  f(x) =", res29, "| Et =", error(true_val, res29))

print("Soal 30 - Newton Forward (x=16, X0=15):")
res30 = newton_forward(x_vals, y_vals, 16, 5)
print("  f(x) =", res30, "| Et =", error(true_val, res30))

print("Soal 31 - Newton Backward (x=16, X0=15):")
res31 = newton_backward(x_vals, y_vals, 16, 5)
print("  f(x) =", res31, "| Et =", error(true_val, res31))
