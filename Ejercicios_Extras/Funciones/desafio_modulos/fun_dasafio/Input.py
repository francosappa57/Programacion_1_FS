from fun_dasafio import Validate as fv

def get_int(mensaje, mensaje_error, minimo, maximo, reintentos):
    print(mensaje)
    while reintentos > 0:
        pedir_numero = int(input("Ingresa un numero entero: "))
        resultado = fv.validate_number(pedir_numero, minimo, maximo)
        if resultado == True:
            return pedir_numero
        else:
            print(mensaje_error)
            reintentos -= 1
            if reintentos > 0:
                print(f"Te quedan {reintentos} intentos")
    return None


def get_float(mensaje, mensaje_error, minimo, maximo, reintentos):
    print(mensaje)
    while reintentos > 0:
        pedir_numero = float(input("Ingresa un numero decimal: "))
        resultado = fv.validate_number(pedir_numero, minimo, maximo)
        if resultado == True:
            return pedir_numero
        else:
            print(mensaje_error)
            reintentos -= 1 
            if reintentos > 0:
                print(f"Te quedan {reintentos} intentos")
    return None


def get_string(mensaje_error, longitud, reintentos):
    while reintentos > 0:
        resultado = fv.validate_length(longitud)
        if resultado == True:
            return "Acceso concedido"
        else:
            print(mensaje_error)
            reintentos -= 1 
            if reintentos > 0:
                print(f"Te quedan {reintentos} intentos")
    return None
        
