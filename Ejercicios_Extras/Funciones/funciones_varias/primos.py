def calcular(numero):
    cantidad_primos = 0
    for x in range(1, numero + 1):
        divisores = 0
        if numero <= 1:
            break
        else:
            for j in range(1, x + 1):
                if x %j == 0:
                    divisores += 1
        if divisores == 2:
            cantidad_primos += 1
    
    return cantidad_primos
