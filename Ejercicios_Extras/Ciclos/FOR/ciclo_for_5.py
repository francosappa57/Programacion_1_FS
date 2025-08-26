suma = 0
vueltas = 0

for x in range(1, 11):
    numero = int(input("Ingresa un numero: "))
    if numero == 0:
        break
    else:
        suma += numero
        vueltas += 1

promedio = suma / vueltas

print(suma, promedio)