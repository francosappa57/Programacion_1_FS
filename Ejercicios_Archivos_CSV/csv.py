import funciones
import archivos

CANTIDAD_PRODUCTOS = 2
nombre_archivo = "productos.csv"
lista_prodcutos = [] 

while True:
    print("\t\n--- Menu Archivo CSV ---")
    print("1. Crear\n"
          "2. Leer\n"
          "3. Salir")
    opciones = int(input("Elige una opcion: "))

    if opciones == 1:
        funciones.crear_lista_prodcutos(lista_prodcutos, CANTIDAD_PRODUCTOS)
        archivos.crear_archivo(nombre_archivo, lista_prodcutos)
    elif opciones == 2:     
        catalogo = archivos.leer_archivo(nombre_archivo)
        funciones.mostrar_catalogo(catalogo)
    elif opciones == 3:
        print("\nHasta luego!!\n")
        break
    else:
        print("\nOpcion invalida. Intente nuevamente")