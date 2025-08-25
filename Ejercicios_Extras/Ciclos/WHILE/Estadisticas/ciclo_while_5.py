contador = 1
suma = 0

while True:
    numero = float(input("Ingresa un numero: "))
    suma += numero

    if contador == 5:
        break
    else:
        contador += 1


promedio = suma / 5

print(suma, promedio)