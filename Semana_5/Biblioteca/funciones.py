def cargar_libro(lista_libro, lista_copia):
    for i in range(len(lista_libro)):
        ejem = input("Ingresa un libro: ")
        cant = int(input("Ingresa cantidad de ejemplares: "))
        lista_libro[i] = ejem.title()
        lista_copia[i] = cant
        pregunta = input("Queres agregar otro libro? (s/n) ").lower()
        if pregunta == "n":
            break
    return lista_libro, lista_copia 


def mostrar_libros(libro, copia):
    for i in range(len(libro)):
        if libro[i] != "":
            print(f"{libro[i]} -> {copia[i]} copias", end="\n")


def cant_copias(libro, copia):
    print("Lista Libros:")
    for i in libro:
        if i != "":
            print(f". {i}")
    consulta = input("Ingresa titulo a consultar: ").lower()
    
    for i in range(len(libro)):
        if libro[i].lower() == consulta:
            if copia[i] != 0:
                return copia[i]
            else:
                return None


def sin_copias(libro, copia):
    lista_sin_copias = [""] * len(libro)
    contador = 0
    for i in range(len(libro)):
        if libro[i] != "":
            if copia[i] == 0:
                lista_sin_copias[contador] = libro[i]
                contador += 1
    if contador == 0:
        return None
    else:
        return lista_sin_copias

def agregar_titulo(libro, copia):
    cambios = None
    for i in range(len(libro)):
        if libro[i] == "":
            nuevo_libro = input("Ingresa nuevo libro: ").title()
            nueva_copia = int(input("Ingresa cantidad de copias: "))
            libro[i] = nuevo_libro
            copia[i] = nueva_copia
            cambios = 1
            return cambios

       
def actualizar(libro, copia):
    print("Lista Libros:")
    for i in libro:
        if i != "":
            print(f". {i}")
    modif = input("Que libro queres modificar? ").lower()
    
    for i in range(len(libro)):
        if libro[i].lower() == modif:
            cambiar_cant = int(input("Ingresa nueva cantidad: "))
            copia[i] = cambiar_cant
            print("Copia modificada")
