import numpy as np

def newton_interpolation(x_data, y_data, x_value):
    n = len(x_data)
    diff_table = np.zeros((n, n))
    diff_table[:,0] = y_data

    for j in range(1, n):
        for i in range(n-j):
            diff_table[i][j] = (diff_table[i+1][j-1] - diff_table[i][j-1]) / (x_data[i+j] - x_data[i])

    result = diff_table[0][0]
    product_term = 1.0
    for i in range(1, n):
        product_term *= (x_value - x_data[i-1])
        result += diff_table[0][i] * product_term

    return round(result, 2)

x_data = [8, 10, 12, 14]
y_data = [660, 1326, 2280, 3570]
x_value = 11

estimated_value = newton_interpolation(x_data, y_data, x_value)
print(f"Taksiran f({x_value}) = {estimated_value}")
