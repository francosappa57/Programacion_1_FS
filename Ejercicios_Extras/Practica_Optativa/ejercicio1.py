numero_entero = int(input("Ingresa un numero entero: "))

print("\t---Numeros pares---")
for x in range(1, numero_entero+1):
    if x %2 == 0:
        print(x, end=" ")

