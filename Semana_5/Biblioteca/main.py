import funciones as f
CANT_LIBROS = 20
array_libros = [""] * CANT_LIBROS
array_copias = [0] * CANT_LIBROS

while True:
    print("\t---Biblioteca---")
    print("1. Cargar libro y cantidad\n"
          "2. Mostrar Catalogo\n"
          "3. Mostrar cantidad de copias\n"
          "4. Ver libros agotados\n"
          "5. Agregar nuevo libro\n"
          "6. Actualizar cantidad copias libros\n"
          "7. Salir")
    datos = int(input("Elige una opcion: "))

    if datos == 1:
        f.cargar_libro(array_libros, array_copias) 
    elif datos == 2:
        f.mostrar_libros(array_libros, array_copias)
    elif datos == 3:
        resultado = f.cant_copias(array_libros, array_copias)
        if resultado == None:
            print(f"Sin copias")
        else:    
            print(f"Quedan {resultado} copia/s")
    elif datos == 4:
        lista = f.sin_copias(array_libros, array_copias)
        if lista == None:
            print("Todos los libros tienen copias disponibles")
        else:
            print("Libros sin copias:")
            for i in lista:
                if i != "":
                    print(f". {i}")   
    elif datos == 5:
        resultado = f.agregar_titulo(array_libros, array_copias)
        if resultado == None:
            print("No se pueden agregar mas titulos")
        else:
            print("Titulo agregado")
    elif datos == 6:
        f.actualizar(array_libros, array_copias)
    elif datos == 7:
        break





            