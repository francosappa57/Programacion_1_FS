def cargar_datos(matriz, s, h):
    for fila in range(s):
        for columna in range(h):
            dato = int(input("Ingresa una temperatura: "))
            matriz[fila][columna] = dato
            

def mostrar_promedio_dias(matriz, s, h):
    acumulador = [0] * 7
    for fila in range(s):
        for columna in range(h):
            acumulador[fila] += matriz[fila][columna]
    
    prom_dia = [0] * 7
    for x in range(len(acumulador)):
        promedio = acumulador[x] / h
        prom_dia[x] = promedio
    return prom_dia


def mostrar_promedio_semanal(matriz, s, h):
    acumulador = 0
    for fila in range(s):
        for columna in range(h):
            acumulador += matriz[fila][columna]
    prom_semana = acumulador / s
    return prom_semana
    