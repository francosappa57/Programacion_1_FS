def es_par(num):
    if num %2 == 0:
        valor = True
    else:
        valor = False
    
    return valor

numero = int(input("Ingresa un numero: "))
resultado = es_par(numero)

if resultado == True:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")
    