CANTIDAD = 10
lista_alumnos = [""] * CANTIDAD
lista_libros = [0] * CANTIDAD
lista_comentarios = [""] * CANTIDAD

# ---- Validacion e ingreso de datos de los alumnos ----
def validar_alumnos(mensaje):
    alumno = ""
    while alumno == "":
        alumno = input(mensaje)
        if alumno == "":
            print("- ERROR. No se puede dejar el espacio en blanco")
    return alumno

def validar_cant_libros(mensaje):
    while True:
        cant_leidos = int(input(mensaje))
        if cant_leidos < 1 or cant_leidos > 20:
            print("- ERROR. La cantidad de libros leidos tiene que ser de 1 a 20")
        else:
            break
    return cant_leidos

def validar_comentario(mensaje):
    opinion = ""
    while opinion == "":
        opinion = input(mensaje)
        if opinion == "":
            print("- ERROR. No puede estar en blanco")
    return opinion

def ingresar_datos(alumnos, libros_leidos, comentario, registro):
    if registro == CANTIDAD:
        print("No se pueden registrar mas alummnos")
        return
    while registro < CANTIDAD:
        print(f"\nRegistro Alumno {registro + 1}")
        alumnos[registro] = validar_alumnos("Ingresa nombre del alumno: ").title()
        libros_leidos[registro] = validar_cant_libros("Ingresa cantidad de libros leidos (1 a 20): ")
        comentario[registro] = validar_comentario("Ingresa comentario sobre los libros leidos: ").upper()
        print("Alumno registrado exitosamente")
        registro += 1

        if registro == 10:
            print("Gracias")
            break
        else:
            pregunta = input("\nDesea agregar otro alumno?(s/n) ").lower()
            if pregunta == "n":
                print("Gracias")
                break
    return registro


# ---- Mostrar alumnos y su promedio ----
def mostrar_alumnos(alumnos, libros_leidos, comentario, registro):
    if registro == 0:
        print("\nSin registro de alumnos")
        return
    print("\n--- Lista de Alumnos Registrados ---")
    for i in range(registro):
        print(f"\nAlumno {i + 1}")
        print(f"Nombre: {alumnos[i]}\n"
              f"Cantidad de libros leidos: {libros_leidos[i]}\n"
              f"Comentario: {comentario[i]}")

def calcular_promedio(libros_leidos, registro):
    suma = 0
    if registro == 0:
        return
    for j in range(registro):
        suma += libros_leidos[j]
    promedio = suma / registro
    print(f"\nEl promedio de libros leidos por los alumnos es de {promedio:.2f}")


# ---- Mostrar alumnos registrados en orden decreciente ----
def ordenar_alumnos(alumnos, libros_leidos, comentario, registro):
    if registro == 0:
        print("\nSin registro de alumnos")
        return
    for i in range(registro - 1):
        intercambio = False
        for j in range(registro - i - 1):
                if libros_leidos[j] < libros_leidos[j + 1]:
                    libros_leidos[j], libros_leidos[j + 1] = libros_leidos[j + 1], libros_leidos[j]
                    alumnos[j], alumnos[j + 1] = alumnos[j + 1], alumnos[j]
                    comentario[j], comentario[j + 1] = comentario[j + 1], comentario[j]
                    intercambio = True
        if intercambio == False:
            break
    print(f"\n---- Lista Registro Alumnos (Orden decreciente) ----")
    for x in range(registro):
        print(f"\nAlumno {x + 1}")
        print(f"Nombre: {alumnos[x]}\n"
              f"Cantidad de libros leidos: {libros_leidos[x]}\n"
              f"Comentario: {comentario[x]}")


# ------------------------------------------------------------------------------------------------------------
registro = 0

while True:
    print("\n--- Menú Habitos de Lectura ---")
    print("1. Ingresar datos de alumno/s")
    print("2. Mostrar alumnos registrados y promedio")
    print("3. Mostrar alumnos en orden decendente segun cantidad de libros leidos")
    print("4. Salir")
    opcion = input("Elija una opcion (1-4): ")
    
    if opcion == "1":
        registro = ingresar_datos(lista_alumnos, lista_libros, lista_comentarios, registro)
    elif opcion == "2":
        mostrar_alumnos(lista_alumnos, lista_libros, lista_comentarios, registro)
        calcular_promedio(lista_libros, registro)
    elif opcion == "3":
        ordenar_alumnos(lista_alumnos, lista_libros, lista_comentarios, registro)
    elif opcion == "4":
        print("Hasta Luego!!!")
        break
    else:
        print("Opcion incorrecta. Intente nuevamente.") 