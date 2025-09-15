import funciones as f

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
        ejem, cant = f.cargar_libro() 
    elif datos == 2:
        f.mostrar_libros(ejem, cant)
    elif datos == 3:
        pedir_titulo = input("Ingresa titulo a consultar: ")
        f.disponible(pedir_titulo, ejem, cant)
    elif datos == 4:
        f.sin_copias(ejem, cant)
    elif datos == 5:
        f.agregar_titulo(ejem, cant)
    elif datos == 6:
        print(ejem)
        pedir_libro = input("Que libro queres modificar? ")
        f.actualizar(pedir_libro, ejem, cant)
    elif datos == 7:
        break





            