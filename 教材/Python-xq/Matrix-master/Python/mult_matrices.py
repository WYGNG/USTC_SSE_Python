import matplotlib.pyplot as plt
from time import time

x = []
y = []

for col_row in range(10, 200, 10):

    print(col_row)

    # se crean las matrices por cada iteracion
    matriz1 = [[1 for i in range(col_row)] for n in range(col_row)]  # crear matriz 1
    matriz2 = [[2 for i in range(col_row)] for n in range(col_row)]  # crear matriz 2
    matriz3 = [[0 for i in range(col_row)] for n in range(col_row)]  # crear matriz 3 que es la que tendra el resultado

    # se hace la multiplicacion de matrices 10 veces para sacar un promedio
    prom = 0  # acumulador se inicia en 0
    for l in range(10):
        time_i = time()
        for i in range(col_row):
            for j in range(col_row):
                matriz3[i][j] = 0
                for k in range(col_row):
                    matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
        time_f = time()
        time_e = time_f - time_i
        elementos = col_row * col_row
        t = time_e / ((col_row * elementos) + ((col_row - 1) * elementos))
        prom += t

    prom = prom / 10
    x.append(col_row)
    y.append(prom)

plt.title('Multiplicación de matrices sin Numpy')
plt.xlabel('Tamaño matrices')
plt.ylabel('Tiempo promedio por operación')
print(x)
print(y)

plt.plot(x, y)
plt.show()
