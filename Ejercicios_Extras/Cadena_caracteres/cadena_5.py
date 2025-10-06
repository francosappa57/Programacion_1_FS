def sup_vocales_rep(cadena):
    nueva = ""
    for i in cadena:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            nueva += i
    return nueva

palabra = input("Ingrese una palabra: ").lower()
print(f"Antes {palabra.upper()}")
nueva_pal = sup_vocales_rep(palabra)
print(f"Despues {nueva_pal.upper()}") 