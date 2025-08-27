def primo(numero):
    divisores = 0
    for x in range(1, numero + 1):
        if numero %x == 0:
            divisores += 1
    if divisores == 2:
        valor = True
    else:
        valor = False
    return valor

num_primo = int(input("Ingresa un numero entero positivo: "))
resultado = primo(num_primo)

if resultado == True:
    print(f"El {num_primo} es primo")
else:
    print(f"El {num_primo} no es primo")
    