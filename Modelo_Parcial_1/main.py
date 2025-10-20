CANTIDAD = 10
lista_personas = [""] * CANTIDAD
lista_puntuaciones = [0] * CANTIDAD
lista_comentarios = [""] * CANTIDAD


def ingresar_datos(personas, puntuacion, comentario):
    for x in range(len(personas)):
        print("")
        while True:
            nombre = input("Ingrese nombre y apellido: ")
            if nombre == "":
                print("-ERROR. Nombre no puede estar en blanco")
            else:
                personas[x] = nombre.title()
                break
        
        while True:
            numero = int(input("Cual fue su puntuacion de satisfaccion? "))
            if numero < 1 or numero > 10:
                print("-ERROR. La puntuacion tiene que ser de 1 a 10")
            else:
                puntuacion[x] = numero
                break
        
        while True:
            opinion = input("Deje un comentario: ")
            if opinion == "":
                print("-ERROR. Comentario no puede estar en blanco")
            else:
                comentario[x] = opinion.capitalize()
                break
    
        print(f"\nParticipante {x + 1}")
        print(f"Nombre: {personas[x]}\n"
              f"Puntuacion: {puntuacion[x]}\n"
              f"Comentario: {comentario[x]}")
        pregunta = input("Desea agreagr otro participante?(s/n) ").lower()
        if pregunta == "n":
            break


def mostrar_participantes(personas, puntuacion, comentario):
    print("\n---Lista de participantes---")
    for i in range(len(personas)):
        if personas[i] == '':
            break
        else:
            print(f"\nParticipante {i + 1}")
            print(f" Nombre: {personas[i]}\n"
                  f" Puntuacion: {puntuacion[i]}\n"
                  f" Comentario: {comentario[i]}")


def calcular_promedio(puntuacion):
    suma = 0
    contador = 0
    for j in range(len(puntuacion)):
        if puntuacion[j] == 0:
            break
        else:
            suma += puntuacion[j]
            contador += 1
    promedio = suma / contador
    print(f"\nEl promedio es de {promedio:.2f}")


def ordenar(persona, puntuacion, comentario):
    largo = len(puntuacion)
    for i in range(largo):
        intercambio = False
        for j in range(largo - i - 1):
            if puntuacion[j + 1] != 0:
                if puntuacion[j] > puntuacion[j + 1]:
                    puntuacion[j], puntuacion[j + 1] = puntuacion[j + 1], puntuacion[j]
                    persona[j], persona[j + 1] = persona[j + 1], persona[j]
                    comentario[j], comentario[j + 1] = comentario[j + 1], comentario[j]
                    intercambio = True
        if intercambio == False:
            break

while True:
    print("\n--- Menú Encuesta de Satisfacción ---")
    print("1. Ingresar participantes")
    print("2. Mostrar participantes y promedio")
    print("3. Ordenar(menor a mayor) participantes por puntuación")
    print("4. Salir")
    seleccion = input("Seleccione una opción (1-4): ")
    
    if seleccion == "1":
        ingresar_datos(lista_personas, lista_puntuaciones, lista_comentarios)
    elif seleccion == "2":
        mostrar_participantes(lista_personas, lista_puntuaciones, lista_comentarios)
        calcular_promedio(lista_puntuaciones)
    elif seleccion == "3":
        ordenar(lista_personas, lista_puntuaciones, lista_comentarios)
    elif seleccion == "4":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
