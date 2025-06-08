import numpy as np

x_sebelum = 5

x_sesudah = np.sqrt((x_sebelum**3 / -6) + (19 * x_sebelum / 6) + 14)

for iterasi in range(5):
    galat_rel = abs(x_sesudah - x_sebelum) * 100 / x_sesudah

    x_sebelum = np.sqrt((x_sebelum**3 / -6) + (19 * x_sebelum / 6) + 14)
    x_sesudah = np.sqrt((x_sesudah**3 / -6) + (19 * x_sesudah / 6) + 14)

    print(f"Iterasi ke-{iterasi + 1} : x = {np.round(x_sebelum, 2)}")
    print(f"Ea = {np.round(galat_rel, 2)}%")
    print()
