# Mayor y su posición

numeros_enteros = [9, 64, 520, 2, 14, 45, 0]
numero_mayor = 0
indice = 0

for x in range(len(numeros_enteros)):
    if numeros_enteros[x] > numero_mayor:
        numero_mayor = numeros_enteros[x] 
        indice = x

print(f"El numero mas alto de la lista es {numero_mayor} y se encuentra en el index {indice}")
