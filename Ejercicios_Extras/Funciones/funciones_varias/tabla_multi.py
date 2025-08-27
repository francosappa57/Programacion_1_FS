def tabla_multiplicar(numero, ini=1, fin=10):
    print(f"----Tabla de multiplicar de {numero}----")
    for x in range(ini, fin + 1):
        resultado = numero * x
        print(f"{numero} x {x} = {resultado}")
