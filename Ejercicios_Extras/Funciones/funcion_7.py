def par_o_impar(numero):
    if numero %2 == 0:
        valor = True
    else:
        valor = False
    return valor

num = int(input("Ingresa un numero entero: "))
valor = par_o_impar(num)

if valor == True:
    print(f"El {num} es par")
else:
    print(f"El {num} es impar")