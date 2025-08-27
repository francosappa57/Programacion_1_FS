import funciones_varias.tabla_multi as ft

numero = int(input("Ingresa un numero entero: "))
inicio = int(input("Ingresa numero inicio (si quieres): "))
final = int(input("Ingresa numero final (si quieres): "))

if inicio == None or final == None:
    pass
    ft.tabla_multiplicar(numero, inicio, final)
else:
    ft.tabla_multiplicar(numero, inicio, final)