import numpy as np

def gauss_seidel(iterasi=2):
    a0, a1, a2 = 0.0, 0.0, 0.0

    print("Iterasi ke-\ta0\t\ta1\t\ta2")
    for i in range(1, iterasi + 1):
        a0 = round((-44 + 3*a1 + 4*a2) / 2, 2)
        a1 = round((78 + 3*a0 + 2*a2) / 9, 2)
        a2 = round((21 + 5*a0 + a1) / 3, 2)
        print(f"{i}\t\t{a0:.2f}\t\t{a1:.2f}\t\t{a2:.2f}")

gauss_seidel()

