suma_positivos = 0
suma_negativos = 0
contador = 0

while True:
    numeros = float(input("Ingresa un numero (positivo o negativo): "))
    if numeros < 0:
        suma_negativos += numeros
        contador += 1
    else:
        suma_positivos += numeros
    
    pregunta = input("Quieres agregar otro numero? (s/n)\n")
    if pregunta == "n":
        break

promedio_negativos = suma_negativos / contador

print(suma_positivos, promedio_negativos)
