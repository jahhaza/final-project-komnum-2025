import numpy as np

def gauss_jordan_stepwise(matrix, max_iter=6):
    matrix = np.array(matrix, dtype=float)
    rows, cols = matrix.shape
    print("Matriks awal:")
    print(np.round(matrix, 2))

    for iteration in range(max_iter):
        if iteration >= rows:
            break  
        i = iteration  
        pivot = matrix[i][i]
        if pivot != 0:
            matrix[i] = matrix[i] / pivot

        for j in range(rows):
            if i != j:
                factor = matrix[j][i]
                matrix[j] = matrix[j] - factor * matrix[i]

        print(f"\nIterasi ke-{iteration + 1}:")
        print(np.round(matrix, 2))

    solution = matrix[:, -1]
    print("\nHasil akhir (a0, a1, a2):")
    print(np.round(solution, 2))
    return np.round(solution, 2)

aug_matrix = [
    [5, 25, 135, 485],
    [25, 135, 775, 2785],
    [135, 775, 4659, 16751]
]

gauss_jordan_stepwise(aug_matrix, max_iter=6)
