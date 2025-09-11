num_secreto = 37

print("\tAdivina el numero")
while True:
    numero = int(input("Ingresa un numero: "))
    if numero > num_secreto:
        print("El numero ingresado es mayor")
    elif numero < num_secreto:
        print("El numero ingresado es menor")
    else:
        print("ADIVINASTE!!!!")
        break

