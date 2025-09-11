numero = int(input("Ingresa numero entero: "))
divisores = 0

if numero <= 1:
    print("El numero tiene que ser mayor a 1") 
else:
    for x in range(1, numero+1):
        if numero %x == 0:
            divisores += 1
    if divisores == 2:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")

