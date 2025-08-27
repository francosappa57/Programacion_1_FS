numero = int(input("Ingresa un numero entero: "))
cantidad_primos = 0

for x in range(1, numero + 1):
    divisores = 0
    if numero <= 1:
        break
    else:
        for j in range(1, x + 1):
            if x %j == 0:
                divisores += 1
    if divisores == 2:
        print(x)
        cantidad_primos += 1

if numero <= 1:
    print("El numero tiene que ser mayor a 1")
else:
    print(f"Cantidad de primos: {cantidad_primos}")