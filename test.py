import numpy as np


# Количество клеток по вертикали и горизонтали
rows, cols = 5, 5

# Коэффициент обесценивания
gamma = 0.9

# Штраф за шаг за пределы поля
penalty = -1

# Создаем матрицу коэффициентов
A = np.zeros((rows * cols, rows * cols))
b = np.zeros(rows * cols)

for i in range(rows):
    for j in range(cols):
        index = i * cols + j  # Индекс текущей клетки в одномерном представлении
        A[index, index] = 1  # Коэффициент при V(s)
        
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]  # Соседние клетки

        # Заполняем вектор свободных членов
        if (i, j) == (0, 1):  # Клетка A
            next_index = 4 * cols + 1  # индекс A`
            A[index, next_index] = (-1)*gamma
            b[index] = 10
        elif (i, j) == (0, 3):  # Клетка B
            next_index = 2 * cols + 3  # индекс B`
            A[index, next_index] = (-1)*gamma
            b[index] = 5
        else:
            for neighbor_i, neighbor_j in neighbors:
                if 0 <= neighbor_i < rows and 0 <= neighbor_j < cols:
                    neighbor_index = neighbor_i * cols + neighbor_j
                    A[index, neighbor_index] -= gamma * 0.25  # Дисконтирование
                else:
                    # Штраф за выход за пределы поля
                    A[index, index] -= gamma * 0.25 
                    b[index] += penalty * 0.25  # Штраф добавляется к вектору свободных членов


# Решаем систему уравнений
V = np.linalg.solve(A, b)

# Выводим результаты
V_matrix = V.reshape((rows, cols))
print("Функции ценности состояния:")
print(V_matrix)