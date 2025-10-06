colores = ('rojo', 'verde', 'azul')

if not "amarillo" in colores:
    lista = list(colores)
    lista.append("amarillo")
    tupla = tuple(lista)
    print(tupla)
else:
    print("El color amarillo esta en la tupla")