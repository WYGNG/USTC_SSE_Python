import numpy as np
from time import time
import matplotlib.pyplot as plt
x = []
y = []
for col_row in range (10, 200, 10):
    matriz1 = np.ones((col_row,col_row))
    matriz2 = np.zeros((col_row,col_row))
    matriz3 = np.zeros((col_row, col_row))

    for i in range(col_row):
        matriz2[0][i] = 2
        matriz2[1][i] = 2

    prom = 0

    for m in range(10):
        time_i = time()
        matriz3 = np.dot(matriz1,matriz2)
        time_f = time()
        time_e = time_f - time_i
        elementos = col_row * col_row
        t = time_e / ((col_row * elementos) + ((col_row - 1) * elementos))
        prom += t

    prom = prom / 10
    x.append(col_row)
    y.append(prom)

plt.title('Multiplicación de matrices con Numpy')
plt.xlabel('Tamaño matrices')
plt.ylabel('Tiempo promedio por operación')
print(x)
print(y)

plt.plot(x, y)
plt.show()
