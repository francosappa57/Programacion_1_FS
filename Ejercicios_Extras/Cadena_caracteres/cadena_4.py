def sup_repetidos(cadena):
    nueva = ""
    for i in cadena:
        if not i in nueva:
            nueva += i
    return nueva

palabra = input("Ingrese una palabra: ").lower()
print(f"Antes {palabra.upper()}")
nueva_pal = sup_repetidos(palabra)
print(f"Despues {nueva_pal.upper()}") 