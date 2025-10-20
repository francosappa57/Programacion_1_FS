def monstrar_tema(canciones):
    print("\n--- Temas de Lady Gaga ---")
    for i in range(len(canciones)):
        print(f"Titulo: {canciones[i]["Tema"]} - Duracion: {canciones[i]["Duracion"]}")
    

def ordenar_por_duracion(canciones):
    for i in range(len(canciones)):
        validar = False
        for j in range(len(canciones) -i -1):
            if canciones[j]["Duracion"] < canciones[j + 1]["Duracion"]:
                canciones[j], canciones[j + 1] = canciones[j + 1], canciones[j]
                validar = True
        if validar == False:
            break


def promedio_por_visitas(canciones):
    total = 0
    for i in canciones:
        total += i["Vistas"] 
    
    promedio = total / len(canciones)
    print(f"\nEl promedio de 'VISTAS X VIDEO' es de {promedio:.2f} millones")


def video_mas_visto(canciones):
    indice = None
    vistas = 0
    for i in range(len(canciones)):
        if canciones[i]["Vistas"] > vistas:
            vistas = canciones[i]["Vistas"]
            indice = i
    print("\n--- Tema mas visto ---")
    for i, j in canciones[indice].items():
        print(f"{i}: {j}")


def video_menos_visto(canciones):
    indice = None
    vistas = 0
    for i in range(len(canciones)):
        if vistas == 0:
            vistas = canciones[i]["Vistas"]
            indice = i
        else:
            if canciones[i]["Vistas"] < vistas:
                vistas = canciones[i]["Vistas"]
                indice = i
    print("\n--- Tema menos visto ---")
    for i, j in canciones[indice].items():
        print(f"{i}: {j}")


def buscar_tema_url(canciones):
    indice = None
    codigo = input("\nIngrese URL a buscar: ")
    for i in canciones:
        if codigo in i["Link Youtube"]:
            indice = canciones.index(i)
    print("\n--- Info ---")
    for i, j in canciones[indice].items():
        print(f"{i}: {j}")
    





    

