def par_o_impar(numero):
    if numero %2 == 0:
        print(f"El {numero} es par")
    else:
        print(f"El {numero} es impar")

num = int(input("Ingresa un numero entero: "))
par_o_impar(num)