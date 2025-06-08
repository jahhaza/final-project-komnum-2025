import numpy as np

def f(x):
    return x**3 + 6*x**2 - 19*x - 84

def false_position(xl, xu, x_true):
    results = []
    xr_old = None
    iterasi = 0

    while True:
        fxl = f(xl)
        fxu = f(xu)

        if fxl * fxu > 0:
            print("Fungsi tidak memenuhi syarat metode posisi salah (tanda f(xl) dan f(xu) harus berbeda).")
            break

        xr = xu - ((fxu * (xl - xu)) / (fxl - fxu))
        xr = round(xr, 2)
        Et = round(abs(x_true - xr), 2)
        
        results.append({
            'iterasi': iterasi + 1,
            'xr': xr,
            'Et': Et,
            'xl': xl,
            'xu': xu
        })

        if 0 <= Et < 1:
            break

        if f(xr) * fxl < 0:
            xu = xr
        else:
            xl = xr

        iterasi += 1

    return results

xl = -1
xu = 8
x_true = 4

hasil_iterasi = false_position(xl, xu, x_true)

for hasil in hasil_iterasi:
    print(f"Iterasi {hasil['iterasi']}: xr = {hasil['xr']}, Et = {hasil['Et']}, xl = {hasil['xl']}, xu = {hasil['xu']}")
