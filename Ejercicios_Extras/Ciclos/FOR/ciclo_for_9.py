numero = int(input("Ingresa un numero: "))
cantidad_divisores = 0

for x in range(1, numero + 1):
    if numero %x == 0:
        print(f"Divisores: {x}")
        cantidad_divisores += 1

print(f"Cantidad Divisores: {cantidad_divisores}")
