# Sumar todos los elementos

vec_numeros = [23, 45, 8, 9, 6, 32, 47, 11, 2, 7]
suma = 0

for x in range(len(vec_numeros)):
    suma += vec_numeros[x]

print(f"La suma es {suma}")
