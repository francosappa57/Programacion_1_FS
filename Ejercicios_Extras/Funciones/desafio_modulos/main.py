import fun_dasafio.Input as fi

mensaje = "--Solicitud de datos--"
mensaje_error = "Clave incorrecta"
minimo = 10
maximo = 32
reintentos = 3

print("1- Clave numero entero\n"
      "2- Clave numero decimal\n"
      "3- Clave palabra")
usuario = int(input("Elige una opcion: "))

if usuario == 1:
    respuesta_int = fi.get_int(mensaje, mensaje_error, minimo, maximo, reintentos)
    print(respuesta_int)
elif usuario == 2:
    respuesta_float = fi.get_float(mensaje, mensaje_error, minimo, maximo, reintentos)
    print(respuesta_float)
else:
    while reintentos > 0:
        palabra = fi.clave()
        respuesta_string = fi.get_string(palabra)
        if respuesta_string != None:
            print(respuesta_string)
            break
        else:
            if reintentos > 1:
                print(mensaje_error)
                print(f"Te quedan {reintentos - 1} intentos")
            else: 
                print(respuesta_string)
        reintentos -= 1