numero = 0
suma_pares = 0

while numero <= 10:
    if numero %2 == 0:
        suma_pares += numero
    numero += 1

print(suma_pares)