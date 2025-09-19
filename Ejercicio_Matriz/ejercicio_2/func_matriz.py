def inicio_torneo(matriz, equipo, ronda):
    for i in range(equipo):
        if i == 0:
            print(f". Equipo {i + 1}")
        else:
            print(f"\n. Equipo {i + 1}")
        for j in range(ronda):
            validar = False
            while validar == False:
                puntaje = int(input(f"Puntaje Ronda {j + 1}: "))
                if puntaje >= 0:
                    matriz[i][j] = puntaje
                    validar = True
                else:
                    print("No se pueden tener puntaje negativo")


def puntaje_total_equipo(matriz, equipo, ronda):
    puntaje_total = [0] * equipo
    for i in range(equipo):
        for j in range(ronda):
            puntaje_total[i] += matriz[i][j]
    return puntaje_total


def ganador(total):
    equipo = None
    puntaje_mayor = 0
    for i in range(len(total)):
        if total[i] >= puntaje_mayor:
            puntaje_mayor = total[i]
            equipo = i + 1
    return equipo, puntaje_mayor
