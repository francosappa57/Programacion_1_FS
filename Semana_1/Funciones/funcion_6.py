def convertir_minutos(minutos):
    hora = 0
    minuto = 0
    for x in range(1, minutos + 1):
        minuto += 1
        if x %60 == 0:
            hora += 1
            minuto -= 60
    return hora, minuto
        
tiempo = int(input("Ingresa la hora en minutos: "))
h, m = convertir_minutos(tiempo)

print(f"{tiempo} minutos equivalen a {h} hora y {m} minutos")