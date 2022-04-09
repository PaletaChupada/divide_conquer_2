'''
Titulo: Calculo de potencia recursiva
Nombre: Daniel Espinoza Bautista
Descripcion: Este programa realiza el calculo de una potencia 'y' a un numero 'x' que el usuario digita
'''

from time import time

def potencia(x,y):
    # Si el valor de la potencia es 0 regresamos uno por la regla
    # de que todo numero elevado a la potencia 0 es 1
    if (y==0):
        return 1
    elif (int(y%2)==0): # Si la potencia es par, realizamos la multiplicacion de las dos llamadas a la funcion 
        return (potencia(x,int(y/2))*potencia(x,int(y/2)))
    else: # Si la potencia no es para multimplicamos el resultado de la primer llamada de la funcion por el numero y a este resultado lo multiplicamos por la segunda llamada de la funcion
        return (x*potencia(x,int(y/2))*potencia(x,int(y/2)))

# Solicitamos al usuario que digite el valor de la potencia
print("¿Que potencia quieres usar?")
pot = int(input())

# Solicitamos al usuario que digite el numero que se elevara a la potencia
print("¿Que numero deseas elevar a la potencia "+"pot"+" ?")
num = int(input())

# Inicializamos la variable tiempo_in que nos ayudara a
# contar el tiempo de ejecucion del programa
tiempo_in = time()

# Realizamos la operacion e imprimimos el resultado
res = potencia(num,pot)
print("El resultado del numero "+str(num)+" a la potencia "+str(pot)+" es: "+str(res))

# Calculamos el tiempo que tardo en encontrarlo
# y lo imprimimos
tiempo_fin = time() - tiempo_in

# Imprimimos el tiempo de ejecucion
print("\nTiempo de ejecucion: %.10f segundos." % tiempo_fin)
    