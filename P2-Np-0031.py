import numpy as np 
# Arevalo Rafael NC:0031 Fceha:22/10/26
# Ejemplos de numpy Numerical Python
print(" --- Espaciado Linealmente en array --- 0031")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print(" --- Matriz identidad en 2D array --- 0031")
Matrix=np.eye(3)
print(Matrix)
print(" --- Genera numeros al azar(Aleatioros) en 2D array --- 0031")
Numale=np.random.random((3,4)) # Genera 12 numeros aleatorios
print(Numale) 
print("Genera 9 numeros aleatorios entre 0 y 1")
Numale=np.random.random((3,3)) # Genera 9 numeros aleatorios
print(Numale)
# como generar 9 números aleatorios comprendidos entre 1 y 20 
# con numpy en un arreglo de 3 por 3
print("generar 9 números aleatorios entre 1 y 20 ")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("Arevalo Rafael NC:0031")
