def tabla_multiplicar(numero, ini="", fin=""):
    if ini == "":
        ini = 1
        fin = int(fin)
        if fin == "":
            fin = 10
    else:
        if fin == "":
            fin = 10
            ini = int(ini)
            if ini == "":
                ini = 1
    
    if ini > fin:
        print("El numero inicial no puede ser mayor al final")
    else:
        print(f"----Tabla de multiplicar de {numero}----")
        for x in range(ini, fin + 1):
            resultado = numero * x
            print(f"{numero} x {x} = {resultado}")
    
