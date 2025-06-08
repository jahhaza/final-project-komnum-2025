import math

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def newton_forward(x, y, x0, h, x_val):
    n = len(y)
    diff_table = [y.copy()]
    for i in range(1, n):
        col = [diff_table[i - 1][j + 1] - diff_table[i - 1][j] for j in range(n - i)]
        diff_table.append(col)

    p = (x_val - x0) / h
    start_idx = x.index(x0)
    result = y[start_idx]

    for i in range(1, n - start_idx):
        term = diff_table[i][start_idx]
        for j in range(i):
            term *= (p - j)
        result += term / factorial(i)

    return round(result, 2)

def newton_backward(x, y, x0, h, x_val):
    n = len(y)
    diff_table = [y.copy()]
    for i in range(1, n):
        col = [diff_table[i - 1][j + 1] - diff_table[i - 1][j] for j in range(n - i)]
        diff_table.append(col)

    p = (x_val - x0) / h
    start_idx = x.index(x0)
    result = y[start_idx]

    for i in range(1, start_idx + 1):
        term = diff_table[i][start_idx - i]
        for j in range(i):
            term *= (p + j)
        result += term / factorial(i)

    return round(result, 2)

def bessel_interpolation(x, y, x0, h, x_val):
    n = len(y)
    diff_table = [y.copy()]
    for i in range(1, n):
        col = [diff_table[i - 1][j + 1] - diff_table[i - 1][j] for j in range(n - i)]
        diff_table.append(col)

    i = x.index(x0)
    p = (x_val - x[i]) / h

    f0 = y[i]
    f1 = y[i + 1]
    delta1 = diff_table[1][i]
    delta2 = diff_table[2][i]
    delta2_1 = diff_table[2][i - 1]
    delta3 = diff_table[3][i - 1]
    delta4 = diff_table[4][i - 2]

    result = (f0 + f1) / 2 + (p - 0.5) * delta1 + \
             ((p * (p - 1)) / 2) * ((delta2 + delta2_1) / 2) + \
             ((p * (p - 1) * (p - 0.5)) / 6) * delta3 + \
             ((p * (p - 1) * (p - 0.5) * (p - 1.5)) / 24) * delta4

    return round(result, 2)

x = [2, 4, 6, 8, 10, 12, 14, 16, 18]
y = [-940, -5068, -6008, -11652, -20980, 2950, 279960, 1581088, 3044340]

h = 2
x_target = 11
x0_forward = 10
x0_backward = 10
x0_bessel = 10
y_true = 154418 

fwd_result = newton_forward(x, y, x0_forward, h, x_target)
bwd_result = newton_backward(x, y, x0_backward, h, x_target)
bessel_result = bessel_interpolation(x, y, x0_bessel, h, x_target)
et_bessel = round(abs(bessel_result - y_true), 2)

print("==== HASIL INTERPOLASI ====")
print(f"33. Newton Gregory Forward (x = 11): {fwd_result}")
print(f"34. Newton Gregory Backward (x = 11): {bwd_result}")
print(f"35. Bessel (x = 11): {bessel_result}")
print(f"    Et (|Y_hasil - Y_sebenarnya|): {et_bessel}")
print(f"36. Newton Gregory Backward (x = 11): {bwd_result}")
