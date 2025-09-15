import funciones as f
CANT_LIBROS = 2
libros = [""] * CANT_LIBROS
copias = [0] * CANT_LIBROS

while True:
    print("---Biblioteca---\n")
    print("1. Cargar libro y cantidad\n",
          "2. Mostrar Catalogo\n",
          "3. Ver libros disponibles\n",
          "4. Ver libros agotados\n",
          "5. Agregar nuevo libro\n",
          "6. Actualizar cantidad libros\n",
          "7. Salir")
    datos = int(input("Elige una opcion: "))

    if datos == 1:
        ejem, cant = f.cargar_libro()
         
    elif datos == 2:
        f.mostrar_libros(ejem, cant)
    elif datos == 3:
        pedir_titulo = input("Ingresa titulo a consultar: ")
        disp = f.disponible(pedir_titulo, ejem, cant)
        print(f"Quedan {disp} copias")
    elif datos == 4:
        sin_copias = f.sin_copias(ejem, cant)
        print("---Libro/s sin copia/s---")
        print(f"{sin_copias}")
    elif datos == 5:




            