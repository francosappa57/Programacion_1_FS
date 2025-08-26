def verificar_acceso(edad):
    if edad >= 18:
        valor = True
    else:
        valor = False
    
    return valor

usuario = int(input("Ingrese su edad: "))
acceso = verificar_acceso(usuario)

if acceso == True:
    print("Acceso concedido")
else:
    print("Acceso denegado. Tiene que ser mayor de 18 años")
