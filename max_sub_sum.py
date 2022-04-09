'''
Titulo: Suma máxima de un subarreglo
Nombre: Daniel Espinoza Bautista
Descripcion: Este programa realiza la suma máxima en un arreglo que el usuario digita a traves de llamadas recursivas 
'''

from time import time

def maxSum(arr,l,m,h):
    # Inicializamos las variables que usaremos para la parte izquierda
    suma = 0
    l_sum = -10000

    for i in range(m,l-1,-1):
        suma = suma + arr[i]
        if suma>l_sum:
            l_sum = suma
    
    # Inicializamos las variables que usaremos para la parte derecha
    suma = 0
    r_sum = -1000

    for i in range(m+1,h+1):
        suma = suma + arr[i]
        if suma>r_sum:
            r_sum = suma
    
    # Retornamos la suma de los elemendos de izquierda a derecha del centro
    return max(l_sum+r_sum,l_sum,r_sum)

def maxSub(arr,l,h):
    # Regresamos el arrelo en caso de que este sea de solo un elemento
    if l==h:
        return arr[l]
    
    # Encontramos el punto medio del subarreglo
    m = (l+h)//2

    # Retornamos la suma maxima en la parte izquierda y derecha y el subarreglo de punto medio
    return max(maxSub(arr,l,m),maxSub(arr,m+1,h),maxSum(arr,l,m,h))

# Inicializamos variables
i=0
arr=[]

# Solicitamos el tamaño del arreglo
print("Dame el tamaño del arrego:")
tam = int(input())

# Inicializamos el ciclo para llenar el arreglo
while i<tam:
    print("Dame el valor de la posicion ["+str(i)+"]")
    aux = int(input())
    arr.append(aux)
    i+=1

# Imprimimos el arreglo
print("Arreglo digitado:"+str(arr))

# Inicializamos la variable tiempo_in que nos ayudara a
# contar el tiempo de ejecucion del programa
tiempo_in = time()

# Realizamos el calculo e imprimimos el resultado
res = maxSub(arr,0,tam-1)
print("La maxima suma contigua es:",res)

# Calculamos el tiempo que tardo en encontrarlo
# y lo imprimimos
tiempo_fin = time() - tiempo_in

# Imprimimos el tiempo de ejecucion
print("\nTiempo de ejecucion: %.10f segundos." % tiempo_fin)
