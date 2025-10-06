def cant_vocales(cadena):
    vocal_a = 0
    vocal_e = 0
    vocal_i = 0
    vocal_o = 0
    vocal_u = 0
    for i in cadena:
        if i == "a":
            vocal_a += 1
        elif i == "e":
            vocal_e += 1
        elif i == "i":
            vocal_i += 1
        elif i == "o":
            vocal_o += 1
        elif i == "u":
            vocal_u += 1
    return vocal_a, vocal_e, vocal_i, vocal_o, vocal_u

palabra = input("Ingrese una palabra: ").lower()
a, e, i, o, u = cant_vocales(palabra)
print(f"Cantidad de vocales en la cadena '{palabra.upper()}'")
print(f"Vocal A: {a}\n"
      f"Vocal E: {e}\n"
      f"Vocal I: {i}\n"
      f"Vocal O: {o}\n"
      f"Vocal U: {u}")