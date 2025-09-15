CANT_LIBROS = 2

def cargar_libro():
    libros = [""] * CANT_LIBROS
    copias = [0] * CANT_LIBROS
    
    for i in range(CANT_LIBROS):
        ejem = input("Ingresa un libro: ")
        cant = int(input("Ingresa cantidad de ejemplares: "))
        libros[i] = ejem
        copias[i] = cant
    return libros, copias


def mostrar_libros(libro, copia):
    for i in range(len(libro)):
        print(f"{libro[i]} -> {copia[i]} copias", end="\n")


def disponible(consulta, libro, copia):
    for i in range(len(libro)):
        if libro[i] == consulta:
            return copia[i]


def sin_copias(libro, copia):
    datos = ""
    for i in range(len(libro)):
        if copia[i] == 0:
            datos += libro[i]
    return datos


def agregar_titulo(libro, copia):
    if len(libro) > CANT_LIBROS:
        cargar_libro
