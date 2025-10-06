def comp_palindromo(cadena):
    for i in range(len(cadena)):
        validar = False
        if cadena[i] == cadena[-i -1]:
            validar = True
        if validar == False:
            return validar
    return validar

palabra = input("Ingrese una palabra: ").lower()
pali = comp_palindromo(palabra)
if pali == False:
    print(f"{palabra.upper()} no es palindromo")
else:
    print(f"{palabra.upper()} es palindromo")