'''
Titulo: Multiplicacion de matrices de Strassen
Nombre: Daniel Espinoza Bautista
Descripcion: Este programa realiza la multiplicacion de 2 matrices (iguales en tamaño) a traves del metodo de Strassen
'''

# Importamos las librerias que usaremos
from time import time
import numpy as np

def strassen(x, y):
    # Si el tamaño de las matrices es 1, simplemente devolvemos la multiplicaciones de 'x' con 'y'
    if x.size == 1 or y.size == 1:
        return x * y

    # Obtenemos el numero de elementos que tiene la matriz x
    n = x.shape[0]

    # Si el numero de elementos es impar rellenamos la matriz con elementos 0 y 1
    if n % 2 == 1:
        x = np.pad(x, (0, 1), mode='constant')
        y = np.pad(y, (0, 1), mode='constant')

    # Obtenemos el tope de la matriz
    m = int(np.ceil(n / 2))

    # Obtenemos cada uno de los elementos
    a = x[: m, : m]
    b = x[: m, m:]
    c = x[m:, : m]
    d = x[m:, m:]
    e = y[: m, : m]
    f = y[: m, m:]
    g = y[m:, : m]
    h = y[m:, m:]

    # Realizamos la llamada recursiva para calcular la multiplicacion de los valores
    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)

    # Ordenamos la matriz con los resultados obtenidos
    result = np.zeros((2 * m, 2 * m), dtype=np.int32)
    result[: m, : m] = p5 + p4 - p2 + p6
    result[: m, m:] = p1 + p2
    result[m:, : m] = p3 + p4
    result[m:, m:] = p1 + p5 - p3 - p7

    # Finalmente retornamos la matriz resultante
    return result[: n, : n]

# Solicitamos al usuario que digite el tamaño de las matrices
print("Dame el tamaño de las matrices (siendo estas de nxn)")
n = int(input())

# Inicializamos las variables y los arreglos
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]   [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
x = [[ 0 for j in range(n)]for i in range(n)]
y = [[ 0 for j in range(n)]for i in range(n)]

# Realizamos el chiclo para llenar las matrices
print("\tMatriz X")
for i in range(n):
    for j in range(n):
        aux = int(input("Dame el valor de la posicion ["+str(i)+"]["+str(j)+"]: "))
        x[i][j]=x[i][j]+aux

print("\tMatriz Y")
for i in range(n):
    for j in range(n):
        aux = int(input("Dame el valor de la posicion ["+str(i)+"]["+str(j)+"]: "))
        y[i][j]=y[i][j]+aux

# Convertimos las matrices a arreglos numpy para poder realizar la multiplicacion
x = np.array(x)
y = np.array(y)

# Imprimimos las matrices a multiplicar
print("\nMatriz X:")
print(x)
print("Matriz Y:")
print(y)

# Inicializamos la variable tiempo_in que nos ayudara a
# contar el tiempo de ejecucion del programa
tiempo_in = time()

# Imprimimos la matriz resultante de la multiplicacion
print("\nMatriz resultante:")
print(strassen(x, y))

# Calculamos el tiempo que tardo en encontrarlo
# y lo imprimimos
tiempo_fin = time() - tiempo_in

# Imprimimos el tiempo de ejecucion
print("\nTiempo de ejecucion: %.10f segundos." % tiempo_fin)