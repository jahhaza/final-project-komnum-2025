import numpy as np

def newton_interpolasi(x_data, y_data, x_taksir):
    n = len(x_data)
    selisih = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        selisih[i][0] = y_data[i]

    for j in range(1, n):
        for i in range(n - j):
            selisih[i][j] = (selisih[i+1][j-1] - selisih[i][j-1]) / (x_data[i+j] - x_data[i])

    print("Tabel Selisih:")
    for i in range(n):
        print([round(selisih[i][j], 2) for j in range(n - i)])

    hasil = selisih[0][0]
    term = 1
    for i in range(1, n):
        term *= (x_taksir - x_data[i-1])
        hasil += selisih[0][i] * term

    return round(hasil, 2)

x_data = [6, 9, 12, 15]
y_data = [234, 960, 2280, 4356]
x_taksir = 11

hasil = newton_interpolasi(x_data, y_data, x_taksir)
print(f"\nTaksiran f({x_taksir}) = {hasil}")
