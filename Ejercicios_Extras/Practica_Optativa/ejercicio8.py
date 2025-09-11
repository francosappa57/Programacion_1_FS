numero = int(input("Ingresa numero entero positivo: "))
factorial = numero

for x in range(numero-1, 0, -1):
    factorial *= x

print(f"El factorial de {numero} es {factorial}")