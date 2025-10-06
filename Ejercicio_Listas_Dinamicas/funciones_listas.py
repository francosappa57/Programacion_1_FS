def agregar_nombre(lista):
    for _ in range(5):
        nombre = input("Ingresa un nombre: ").title()
        lista.append(nombre)


def agregar_nuevo_nombre(lista):
    agregar_nuevo = input("\nInserte un nuevo nombre: ").title()
    lista.insert(1, agregar_nuevo)


def eliminar_nombre(lista):
    eliminar = input("\nIngrese un nombre a eliminar: ").title()
    validar = False
    while validar == False:
        for nombre in lista:
            if nombre == eliminar:
                lista.remove(eliminar)
                print(f"\n{lista}")
                validar = True
        if validar == False:
            print(f"\nEl nombre {eliminar.upper()} no se encuentra en la lista")
            validar = True


def verificar_nombre(lista):
    identificar = input("\nIngresa un nombre a verificar: ").title()
    if identificar in lista:
        print(f"\nEl nombre {identificar.upper()} esta en la lista")
    else:
        print(f"\nEl nombre {identificar.upper()} no se encuentra en la lista")


def mostrar_index(lista):
    buscar = input("\nIngresar nombre a buscar: ").title()
    if buscar in lista:
        indice = lista.index(buscar)
        print(f"\nEl nombre {buscar.upper()} se encuentra en el indice {indice}")
    else:
        print(f"\nEl nombre {buscar.upper()} no se encuentra en la lista")


def agregar_notas():
    notas = []
    for i in range(3):
        print(f"\nNota {i + 1}")
        calificacion = float(input("Cuanto te sacaste? "))
        notas.append(calificacion)
    return notas


def agregar_nueva_nota(lista):
    nueva_nota = float(input("\nIngresa una nueva nota: "))
    lista[3].append(nueva_nota)


def cargar_nuevo_estudiante():
    nuevo_estudiante = []
    print("\n--- Nuevo estudiante ---")
    nombre = input("Nombre: ").title()
    apellido = input("Apellido: ").title()
    dni = int(input("DNI: "))
    nuevo_estudiante.append(nombre)
    nuevo_estudiante.append(apellido)
    nuevo_estudiante.append(dni)
    return nuevo_estudiante


def limpiar_lista(lista):
    lista.clear()
    

