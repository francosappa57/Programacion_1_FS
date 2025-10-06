def indice_caracter(cadena):
    for i in range(len(cadena)):
        if cadena[i] == "-":
            return i
    return -1

palabra = input("Ingresar palabra con caracter(si queres): ").lower()
caracter = indice_caracter(palabra)
if caracter == -1:
    print("No tiene ningun caracter especial")
else:
    print(f"El caracter especial se encuentra en el indice {caracter}")