suma = 0
contador = 0

while True:
    numero = float(input("Ingresa un numero: "))
    suma += numero
    contador += 1

    pregunta = input("Queres agregar otro numero? (s/n)\n").lower()
    if pregunta == "s":
        continue
    else:
        break

promedio = suma / contador
print(suma, promedio)