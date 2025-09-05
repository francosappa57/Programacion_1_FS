def validate_number(numero, minimo, maximo):
    if numero >= minimo and numero <= maximo:
        valor = True
    else:
        valor = False
    return valor

def validate_length(largo):
    if largo > 3 and largo < 10:
        valor = True
    else:
        valor = False
    return valor
    