# Intercambiar elementos pares por ceros

enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(len(enteros)):
    if enteros[x] %2 == 0:
        enteros[x] = 0

print(enteros)