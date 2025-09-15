CANT_LIBROS = 4
libros = [""] * CANT_LIBROS
copias = [0] * CANT_LIBROS

def cargar_libro():
    for i in range(CANT_LIBROS):
        ejem = input("Ingresa un libro: ")
        cant = int(input("Ingresa cantidad de ejemplares: "))
        libros[i] = ejem
        copias[i] = cant
        pregunta = input("Queres agregar otro libro? (s/n) ").lower()
        if pregunta == "n":
            break
    return libros, copias


def mostrar_libros(libro, copia):
    for i in range(len(libro)):
        if libro[i] == "":
            pass
        else:
            print(f"{libro[i]} -> {copia[i]} copias", end="\n")


def disponible(consulta, libro, copia):
    for i in range(len(libro)):
        if libro[i] == consulta:
            print(f"Quedan {copia[i]} copias")


def sin_copias(libro, copia):
    print("Libros sin copias disponibles:")
    for i in range(CANT_LIBROS):
        if libro[i] != "":
            if copia[i] == 0:
                print(libro[i])


def agregar_titulo(libro, copia):
    for i in range(CANT_LIBROS):
        if libro[i] == "":
            nuevo_libro = input("Ingresa nuevo libro: ")
            nueva_copia = int(input("Ingresa cantidad de copias: "))
            libro[i] = nuevo_libro
            copia[i] = nueva_copia
            print("Libro agregado")
        else:
            print("No se pueden agregar nuevos libros")


def actualizar(cambio, libro, copia):
    for i in range(CANT_LIBROS):
        if libro[i] == cambio:
            cambiar_cant = int(input("Ingresa nueva cantidad: "))
            copia[i] = cambiar_cant
            print("Copias modificadas")