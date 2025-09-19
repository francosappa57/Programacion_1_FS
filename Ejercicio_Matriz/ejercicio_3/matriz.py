# Ejercicio 3: Control de Producción
# Una fábrica produce 3 productos y mide la producción durante 4 días.
# Cargar en una matriz 3x4 las cantidades producidas. Mostrar:
#     La producción total de cada producto.
#     La producción total de cada día.
#     Cuál fue el día con mayor producción total.
import func_matriz as fm

PRODUCTOS = 3
DIAS = 4

produccion = [[4, 12, 9, 0],
              [35, 55, 20, 10],
              [9, 23, 98, 8]]

salir = False

while salir == False:
    print("\n---Seguimiento de productos---")
    print("1. Mostrar produccion total x PRODUCTO\n"
          "2. Mostrar produccion total x DIA\n"
          "3. Mostrar mayor dia de produccion\n"
          "4. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        fm.produccion_por_producto(produccion, PRODUCTOS, DIAS)
    elif opcion == "2":
        total = fm.produccion_por_dia(produccion, PRODUCTOS, DIAS)
    elif opcion == "3":
        fm.mayor_dia_produccion(total)
    elif opcion == "4":
        salir = True
