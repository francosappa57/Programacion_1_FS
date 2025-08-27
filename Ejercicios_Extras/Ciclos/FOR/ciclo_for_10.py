numero = int(input("Ingresa un numero entero: "))
divisores = 0

for x in range(1, numero + 1):
    if numero %x == 0:
        divisores += 1

if divisores == 2:
    print(f"El {numero} es primo")
else:
    print(f"El {numero} no es primo")


